def revse_text(text):
    result = []
    splitted = text.split()

    for name in splitted:

        result.append( name[::-1])
    return' '.join(result)

print(revse_text('Umair mufti'))