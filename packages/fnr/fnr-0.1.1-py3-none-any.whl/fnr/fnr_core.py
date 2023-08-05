from .context_loaders import file_loader, console_loader
import re

def load_keywords_to_be_replaced(args):
    if (args.context_file):
        print('Loading the context variables from {} now...'.format(args.context_file))
        context_file = file_loader(args.context_file)
    else:
        context_file = console_loader()

    return context_file.load_context_vars()

def find_and_replace(context, template):
    # escape special regex characters from keys
    context = {re.escape(k):v for k,v in context.items()}
    pattern = re.compile('|'.join(context.keys()))
    return re.sub(pattern, lambda match: context[re.escape(match.group())], template)