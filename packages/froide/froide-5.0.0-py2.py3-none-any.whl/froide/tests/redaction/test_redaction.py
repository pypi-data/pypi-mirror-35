import unittest
import os

from froide.helper.redaction import redact_file


def get_test_file(name):
    return os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'testdata', name
    )


TEXTS = [
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            67,
            71,
            12
        ],
        "text": "Referat MK3 ",
        "transform": "scaleX(0.818861)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "8.66667px",
        "pos": [
            113,
            94,
            204,
            8
        ],
        "text": "Bundesministerium für Ernährung und Landwirtschaft",
        "transform": "scaleX(0.819926)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "8.66667px",
        "pos": [
            113,
            103,
            125,
            8
        ],
        "text": "- Dienstsitz Berlin – 11055 Berlin",
        "transform": "scaleX(0.819653)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            92,
            205,
            12
        ],
        "text": "Internet, Soziale Medien, Medien und  ",
        "transform": "scaleX(0.820193)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            108,
            111,
            12
        ],
        "text": "Kommunikationsstab",
        "transform": "scaleX(0.819631)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            132,
            67,
            12
        ],
        "text": "Beate Müller",
        "transform": "scaleX(0.818345)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            154,
            103,
            16
        ],
        "text": "Nur per E-Mail",
        "transform": "scaleX(0.955506)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            186,
            287,
            16
        ],
        "text": "██████████@fragdenstaat.de",
        "transform": "scaleX(0.889075)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            218,
            40,
            16
        ],
        "text": "Herrn",
        "transform": "scaleX(0.932618)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            234,
            102,
            16
        ],
        "text": "Arne Semsrott",
        "transform": "scaleX(0.907354)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            250,
            237,
            16
        ],
        "text": "c/o Open Knowledge Foundation ",
        "transform": "scaleX(0.912573)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            266,
            120,
            16
        ],
        "text": "Deutschland e.V.",
        "transform": "scaleX(0.901391)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            282,
            122,
            16
        ],
        "text": "Singerstraße 109",
        "transform": "scaleX(0.879558)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            298,
            89,
            16
        ],
        "text": "10179 Berlin",
        "transform": "scaleX(0.933354)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "8.66667px",
        "pos": [
            459,
            160,
            73,
            8
        ],
        "text": "HAUSANSCHRIFT",
        "transform": "scaleX(0.819174)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            157,
            138,
            12
        ],
        "text": "Rochusstr. 1, 53123 Bonn",
        "transform": "scaleX(0.819409)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "8.66667px",
        "pos": [
            507,
            184,
            16,
            8
        ],
        "text": "TEL",
        "transform": "scaleX(0.819069)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            181,
            116,
            12
        ],
        "text": "+49 (0)228 529 -4381",
        "transform": "scaleX(0.820299)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "8.66667px",
        "pos": [
            496,
            201,
            29,
            8
        ],
        "text": "E-MAIL",
        "transform": "scaleX(0.819472)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            198,
            110,
            12
        ],
        "text": "MK3@bmel.bund.de",
        "transform": "scaleX(0.820032)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "8.66667px",
        "pos": [
            484,
            218,
            43,
            8
        ],
        "text": "INTERNET",
        "transform": "scaleX(0.817031)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            215,
            71,
            12
        ],
        "text": "www.bmel.de",
        "transform": "scaleX(0.819873)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "8.66667px",
        "pos": [
            511,
            234,
            11,
            8
        ],
        "text": "AZ",
        "transform": "scaleX(0.824689)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            231,
            60,
            12
        ],
        "text": "MK3-05111",
        "transform": "scaleX(0.820912)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "8.66667px",
        "pos": [
            495,
            268,
            31,
            8
        ],
        "text": "DATUM",
        "transform": "scaleX(0.819833)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "12px",
        "pos": [
            530,
            265,
            65,
            12
        ],
        "text": "7. Juni 2018",
        "transform": "scaleX(0.819273)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            345,
            531,
            16
        ],
        "text": "Antrag auf Informationszugang nach dem Informationsfreiheitsgesetz (IFG)",
        "transform": "scaleX(0.981252)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            393,
            63,
            16
        ],
        "text": "Anlagen:",
        "transform": "scaleX(0.927109)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            172,
            393,
            14,
            16
        ],
        "text": " 1",
        "transform": "scaleX(0.899297)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            433,
            206,
            16
        ],
        "text": "Sehr geehrter Herr Semsrott,",
        "transform": "scaleX(0.89091)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            481,
            572,
            16
        ],
        "text": "mit Ihrer E-Mail vom 20.05.2018 beantragen Sie Aktenauskunft über seitens des ",
        "transform": "scaleX(0.906647)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            505,
            619,
            16
        ],
        "text": "Bundesministeriums für Ernährung und Landwirtschaft (BMEL) über Twitter versendete ",
        "transform": "scaleX(0.922827)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            529,
            423,
            16
        ],
        "text": "Direktnachrichten der Jahre 2014, 2015, 2016, 2017, 2018. ",
        "transform": "scaleX(0.901187)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            577,
            500,
            16
        ],
        "text": "Über Ihren Antrag entscheide ich nach §§ 1 Absatz 1, 10 IFG wie folgt:",
        "transform": "scaleX(0.913616)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            128,
            601,
            9,
            16
        ],
        "text": "I.",
        "transform": "scaleX(1.0492)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            161,
            601,
            185,
            16
        ],
        "text": "Der Antrag wird abgelehnt",
        "transform": "scaleX(0.919461)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            122,
            625,
            13,
            16
        ],
        "text": "II.",
        "transform": "scaleX(1.09899)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            161,
            625,
            244,
            16
        ],
        "text": "Der Bescheid ergeht gebührenfrei.",
        "transform": "scaleX(0.899254)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            673,
            91,
            16
        ],
        "text": "Begründung:",
        "transform": "scaleX(0.911115)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            721,
            32,
            16
        ],
        "text": "Zu I.",
        "transform": "scaleX(0.970263)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            769,
            614,
            16
        ],
        "text": "Das BMEL betreibt seit Mai 2013 einen Twitter-Kanal. Die dort bislang eingegangenen ",
        "transform": "scaleX(0.917575)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            793,
            632,
            16
        ],
        "text": "Direktnachrichten ergaben nicht die Notwendigkeit eines Verwaltungshandelns. Vielmehr ",
        "transform": "scaleX(0.912649)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            817,
            638,
            16
        ],
        "text": "wurden/werden mit anderen Nutzern nur vereinzelte flüchtige Informationen ausgetauscht.",
        "transform": "scaleX(0.908808)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            865,
            612,
            16
        ],
        "text": "Entsprechende Informationen wären erst dann aktenrelevant, wenn die entsprechende",
        "transform": "scaleX(0.892025)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            889,
            554,
            16
        ],
        "text": "Information aufgrund Ihrer besonderen Bedeutung Bestandteil eines Vorgangs",
        "transform": "scaleX(0.90167)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            913,
            435,
            16
        ],
        "text": "würde bzw. ein weiteres Verwaltungshandeln ausgelöst hätte.",
        "transform": "scaleX(0.897569)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            937,
            643,
            16
        ],
        "text": "Dies war hier nicht der Fall, die bisherigen Direktnachrichten waren nicht aktenrelevant, es ",
        "transform": "scaleX(0.912461)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            961,
            500,
            16
        ],
        "text": "handelt sich somit nicht um amtliche Informationen i.S.d. § 1 Nr. 1 IFG.",
        "transform": "scaleX(0.923431)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            985,
            593,
            16
        ],
        "text": "Ein Informationszugang auf nicht „veraktete“ Kommunikation ist nach dem IFG nicht",
        "transform": "scaleX(0.929862)"
    },
    {
        "fontFamily": "sans-serif",
        "fontSize": "16px",
        "pos": [
            113,
            1009,
            62,
            16
        ],
        "text": "geboten.",
        "transform": "scaleX(0.875769)"
    }
]


class TestRedaction(unittest.TestCase):
    def test_redaction_simple(self):
        filename = get_test_file('test_01.pdf')
        instructions = [
            {
                "height": 1122.6666666666665,
                "pageNumber": 1,
                "rects": [
                    [
                        111,
                        186,
                        170,
                        19.2
                    ]
                ],
                "texts": [],
                "scaleFactor": 1.3333333333333333,
                "width": 793.3333333333333
            },
            {
                "height": 1122.6666666666665,
                "pageNumber": 2,
                "rects": [],
                "scaleFactor": 1.3333333333333333,
                "texts": [],
                "width": 793.3333333333333
            }
        ]
        with open(filename, 'rb') as pdf_file:
            output_filename = redact_file(pdf_file, instructions)
        print(output_filename)
