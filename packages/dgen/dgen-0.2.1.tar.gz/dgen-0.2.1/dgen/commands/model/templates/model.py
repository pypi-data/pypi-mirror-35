class [[ name ]](models.Model):
    class Meta:
        verbose_name = _('[[ name ]]')
        verbose_name_plural = _('[[ name ]]s')
        ordering = ['id']
    [% for field in fields %][[ field ]][% endfor %]

    def __str__(self):
        return f'[[ name ]]{self.id}'
