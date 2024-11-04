import xml.etree.ElementTree as ET

tree = ET.parse("ex_3.xml")
root = tree.getroot()

for item in root.iter("СведТов"):
    attrib = item.attrib
    print(f'Наименование: {attrib["НаимТов"]}\n'
          f'Цена: {attrib["ЦенаТов"]}\n'
          f'Количество: {attrib["КолТов"]}\n'
          f'Стоимость без НДС: {attrib["СтТовБезНДС"]}\n'
          f'НДС: {attrib["НалСт"]}\n'
          f'Стоимость товара с НДС: {attrib["СтТовУчНал"]}\n')