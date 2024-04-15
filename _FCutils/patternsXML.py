TEXT_XML_BASE = '''
<?xml version="1.0" encoding="utf-8"?>
<GameData>
	<LocalizedText>
{replace}
	</LocalizedText>
</GameData>

'''.strip()

TEXT_XML_REPLACE = '''
        <Replace Tag="{tag}" Language="{lang}">
			<Text>{text}</Text>
		</Replace>
'''


XML_BASE = '''
<?xml version="1.0" encoding="utf-8"?>
<GameData>
	{xml}
</GameData>
'''.strip()

XML_TABLE_BASE = '''
	<{table}>
{rows}
	</{table}>
'''

XML_CITIES_TAG_ROW = '''
		<Row CivilizationType="{civType}" CityName="{cityName}"/>'''
  
XML_CUSTOM_COLOR_ROW__CONST = '''
		<Row>
			<Type>COLOR_</Type>
			<Color>0,0,0,0</Color>
		</Row>'''

XML_PLAYERCOLORS_PATTERN_ROW = '''
		<Row>
			<Type>{leader}</Type>
			<Usage>Unique</Usage>
			<PrimaryColor></PrimaryColor>
			<SecondaryColor></SecondaryColor>
			<Alt1PrimaryColor></Alt1PrimaryColor>
			<Alt1SecondaryColor></Alt1SecondaryColor>
			<Alt2PrimaryColor></Alt2PrimaryColor>
			<Alt2SecondaryColor></Alt2SecondaryColor>
			<Alt3PrimaryColor></Alt3PrimaryColor>
			<Alt3SecondaryColor></Alt3SecondaryColor>
		</Row>'''