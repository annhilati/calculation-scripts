def replace_with_unicode_bold(text):
    """
    Ersetzt alle Buchstaben in einem String durch die mathematisch fetten Unicode-Zeichen.
    Unterstützt nur lateinische Buchstaben (a-z, A-Z).

    :param text: Der Eingabestring
    :return: String mit ersetzten Zeichen
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Kleinbuchstaben: Basis + Offset für Unicode-Bold-Kleinbuchstaben
            result.append(chr(ord(char) - ord('a') + 0x1D41A))
        elif 'A' <= char <= 'Z':
            # Großbuchstaben: Basis + Offset für Unicode-Bold-Großbuchstaben
            result.append(chr(ord(char) - ord('A') + 0x1D400))
        else:
            # Andere Zeichen bleiben unverändert
            result.append(char)

    return ''.join(result)

def replace_with_unicode_double_struck(text):
    """
    Ersetzt alle Buchstaben in einem String durch die mathematisch doppelgestrichenen Unicode-Zeichen.
    Unterstützt nur lateinische Buchstaben (a-z, A-Z).

    :param text: Der Eingabestring
    :return: String mit ersetzten Zeichen
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Kleinbuchstaben: Basis + Offset für Unicode-Double-Struck-Kleinbuchstaben
            result.append(chr(ord(char) - ord('a') + 0x1D552))
        elif 'A' <= char <= 'Z':
            # Großbuchstaben: Basis + Offset für Unicode-Double-Struck-Großbuchstaben
            result.append(chr(ord(char) - ord('A') + 0x1D538))
        else:
            # Andere Zeichen bleiben unverändert
            result.append(char)

    return ''.join(result)

def replace_with_unicode_fraktur(text):
    """
    Ersetzt alle Buchstaben in einem String durch die Fraktur Unicode-Zeichen.
    Unterstützt nur lateinische Buchstaben (a-z, A-Z).

    :param text: Der Eingabestring
    :return: String mit ersetzten Zeichen
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Kleinbuchstaben: Basis + Offset für Unicode-Fraktur-Kleinbuchstaben
            result.append(chr(ord(char) - ord('a') + 0x1D51E))
        elif 'A' <= char <= 'Z':
            # Großbuchstaben: Basis + Offset für Unicode-Fraktur-Großbuchstaben
            result.append(chr(ord(char) - ord('A') + 0x1D504))
        else:
            # Andere Zeichen bleiben unverändert
            result.append(char)

    return ''.join(result)

def replace_with_unicode_bold_fraktur(text):
    """
    Ersetzt alle Buchstaben in einem String durch die fetten Fraktur Unicode-Zeichen.
    Unterstützt nur lateinische Buchstaben (a-z, A-Z).

    :param text: Der Eingabestring
    :return: String mit ersetzten Zeichen
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Kleinbuchstaben: Basis + Offset für Unicode-Bold-Fraktur-Kleinbuchstaben
            result.append(chr(ord(char) - ord('a') + 0x1D586))
        elif 'A' <= char <= 'Z':
            # Großbuchstaben: Basis + Offset für Unicode-Bold-Fraktur-Großbuchstaben
            result.append(chr(ord(char) - ord('A') + 0x1D56C))
        else:
            # Andere Zeichen bleiben unverändert
            result.append(char)

    return ''.join(result)

def replace_with_unicode_sans_serif_bold(text):
    """
    Ersetzt alle Buchstaben in einem String durch die fettgedruckten Sans-Serif Unicode-Zeichen.
    Unterstützt nur lateinische Buchstaben (a-z, A-Z).

    :param text: Der Eingabestring
    :return: String mit ersetzten Zeichen
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Kleinbuchstaben: Basis + Offset für Unicode-Sans-Serif-Bold-Kleinbuchstaben
            result.append(chr(ord(char) - ord('a') + 0x1D5EE))
        elif 'A' <= char <= 'Z':
            # Großbuchstaben: Basis + Offset für Unicode-Sans-Serif-Bold-Großbuchstaben
            result.append(chr(ord(char) - ord('A') + 0x1D5D4))
        else:
            # Andere Zeichen bleiben unverändert
            result.append(char)

    return ''.join(result)

def replace_with_unicode_sans_serif_bold_italic(text):
    """
    Ersetzt alle Buchstaben in einem String durch die fettgedruckten kursiven Sans-Serif Unicode-Zeichen.
    Unterstützt nur lateinische Buchstaben (a-z, A-Z).

    :param text: Der Eingabestring
    :return: String mit ersetzten Zeichen
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Kleinbuchstaben: Basis + Offset für Unicode-Sans-Serif-Bold-Italic-Kleinbuchstaben
            result.append(chr(ord(char) - ord('a') + 0x1D63A))
        elif 'A' <= char <= 'Z':
            # Großbuchstaben: Basis + Offset für Unicode-Sans-Serif-Bold-Italic-Großbuchstaben
            result.append(chr(ord(char) - ord('A') + 0x1D620))
        else:
            # Andere Zeichen bleiben unverändert
            result.append(char)

    return ''.join(result)

def replace_with_unicode_small_caps(text):
    """
    Ersetzt alle Buchstaben in einem String durch die Small-Caps Unicode-Zeichen (hochgestellte Kleinbuchstaben).
    Unterstützt nur lateinische Buchstaben (a-z).

    :param text: Der Eingabestring
    :return: String mit ersetzten Zeichen
    """
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            # Kleinbuchstaben: Basis + Offset für Unicode-Small-Caps
            result.append(chr(ord(char) - ord('a') + 0x1D00))
        else:
            # Andere Zeichen bleiben unverändert
            result.append(char)

    return ''.join(result)

# Beispielaufrufe
input_text = "Shitposting"
print("Bold:", replace_with_unicode_bold(input_text))
print("Double-Struck:", replace_with_unicode_double_struck(input_text))
print("Fraktur:", replace_with_unicode_fraktur(input_text))
print("Bold Fraktur:", replace_with_unicode_bold_fraktur(input_text))
print("Sans-Serif Bold:", replace_with_unicode_sans_serif_bold(input_text))
print("Sans-Serif Bold Italic:", replace_with_unicode_sans_serif_bold_italic(input_text))
print("Small Caps:", replace_with_unicode_small_caps(input_text))