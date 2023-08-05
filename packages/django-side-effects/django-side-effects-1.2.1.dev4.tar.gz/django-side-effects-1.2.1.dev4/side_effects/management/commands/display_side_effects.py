import json

from django.core.management.base import BaseCommand

from side_effects.registry import fname, docstring, _registry


class Command(BaseCommand):

    help = "Displays project side_effects."

    def add_arguments(self, parser):
        parser.add_argument(
            '--raw',
            action='store_true',
            help="Display raw mapping of labels to functions."
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            help="Display full docstring for all side-effect functions."
        )
        parser.add_argument(
            '--label',
            action='store',
            dest='label',
            help="Filter side-effects on a single event label"
        )
        parser.add_argument(
            '--label-contains',
            action='store',
            dest='contains',
            help="Filter side-effects on a event labels containing the supplied text"
        )

    def handle(self, *args, **options):
        self.stdout.write("The following side-effects are registered:")
        if options['label']:
            events = {k: v for k, v in _registry.items() if k == options['label']}
        elif options['contains']:
            events = {k: v for k, v in _registry.items() if options['contains'] in k}
        else:
            events = _registry.items()

        if options['raw']:
            self.print_raw(events)
        elif options['verbose']:
            self.print_verbose(events)
        else:
            self.print_default(events)

    def print_raw(self, events):
        """Print out the fully-qualified named for each mapped function."""
        raw = {label: [fname(f) for f in funcs] for label, funcs in events.items()}
        self.stdout.write(json.dumps(raw, indent=4))

    def print_verbose(self, events):
        """Print the entire docstring for each mapped function."""
        for label, funcs in events.items():
            self.stdout.write('')
            self.stdout.write(label)
            self.stdout.write('')
            for func in funcs:
                docs = docstring(func)
                self.stdout.write('  - %s' % docs[0])
                for line in docs[1:]:
                    self.stdout.write('    %s' % line)
                self.stdout.write('')

    def print_default(self, events):
        """Print the first line of the docstring for each mapped function."""
        for label, funcs in events.items():
            self.stdout.write('')
            self.stdout.write(label)
            for func in funcs:
                docs = docstring(func)
                if docs is None:
                    self.stdout.write('*** DOCSTRING MISSING: %s ***' % func.__name__)
                else:
                    self.stdout.write('  - %s' % docs[0])
