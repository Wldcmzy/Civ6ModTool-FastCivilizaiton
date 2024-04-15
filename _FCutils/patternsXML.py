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
	<{table}>
{rows}
	</{table}>
</GameData>
'''.strip()

XML_CITIES_TAG_ROW = '''
		<Row CivilizationType="{civType}" CityName="{cityName}"/>'''