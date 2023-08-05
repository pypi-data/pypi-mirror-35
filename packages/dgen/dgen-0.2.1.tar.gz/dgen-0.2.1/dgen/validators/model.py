import click


def validate_field(ctx, param, value):
    fields = []
    for field in value:
        try:
            ftype, fname = field.split(':')
        except ValueError:
            raise click.BadParameter('field needs to be in format <type:name>, e.g. t:body')
        fields.append((ftype, fname))
    return fields
