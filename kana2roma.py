kana_dict = {
    'ア' : 'a', 'イ' : 'i', 'ウ' : 'u', 'エ' : 'e', 'オ' : 'o',
    'カ' : 'ka', 'キ' : 'ki', 'ク' : 'ku', 'ケ' : 'ke', 'コ' : 'ko',
    'サ' : 'sa', 'シ' : 'shi', 'ス' : 'su', 'セ' : 'se', 'ソ' : 'so',
    'タ' : 'ta', 'チ' : 'chi', 'ツ' : 'tsu', 'テ' : 'te', 'ト' : 'to',
    'ナ' : 'na', 'ニ' : 'ni', 'ヌ' : 'nu', 'ネ' : 'ne', 'ノ' : 'no',
    'ハ' : 'ha', 'ヒ' : 'hi', 'フ' : 'fu', 'ヘ' : 'he', 'ホ' : 'ho',
    'マ' : 'ma', 'ミ' : 'mi', 'ム' : 'mu', 'メ' : 'me', 'モ' : 'mo',
    'ヤ' : 'ya', 'ユ' : 'yu', 'ヨ' : 'yo',
    'ラ' : 'ra', 'リ' : 'ri', 'ル' : 'ru', 'レ' : 're', 'ロ' : 'ro',
    'ワ' : 'wa', 'ヲ' : 'wo', 'ン' : 'n',
    'ガ' : 'ga', 'ギ' : 'gi', 'グ' : 'gu', 'ゲ' : 'ge', 'ゴ' : 'go',
    'ザ' : 'za', 'ジ' : 'ji', 'ズ' : 'zu', 'ゼ' : 'ze', 'ゾ' : 'zo',
    'ダ' : 'da', 'ヂ' : 'ji', 'ヅ' : 'zu', 'デ' : 'de', 'ド' : 'do',
    'バ' : 'ba', 'ビ' : 'bi', 'ブ' : 'bu', 'ベ' : 'be', 'ボ' : 'bo',
    'パ' : 'pa', 'ピ' : 'pi', 'プ' : 'pu', 'ペ' : 'pe', 'ポ' : 'po',
    'ヴ' : 'vu',

    'ァ' : 'la', 'ィ' : 'li', 'ゥ' : 'lu', 'ェ' : 'le', 'ォ' : 'lo',
    'ャ' : 'lya', 'ュ' : 'lyu', 'ョ' : 'lyo',
    'ッ' : 'ltsu'
    }


class Kana2Roma():
    kana_dict = kana_dict
    @classmethod
    def kana2roma(cls, string_array):
        romaji = []
        for moji in string_array:
            romaji.append(cls.kana_dict[moji])
        return romaji
