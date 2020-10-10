# Tool Made in Python 3
# Author https://www.fiverr.com/alifarslan

from csv import DictReader


class ParsingScript:
    def get_products(self):
        try:
            return [dict(e) for e in DictReader(open('products_2.csv'))]
        except Exception as e:
            print(e)

    def parse_csv_to_html(self):
        products = self.get_products()
        html_file = open('data.html', mode="w")

        for p in products:
            template = f"""

    <h6>Description</h6>
    {p['Pattern Name']} {p['Product Description']}
    <h6>Pattern Details</h6>
    <div class="digital-details">
      <ul>
        <li><strong>Format: </strong> {p['Pattern Name']}</li>
        <li><strong>Designer: </strong> {p['Designer']}</li>
        <li><strong>Craft: </strong> {p['Craft']}</li>
        <li><strong>Skill Level: </strong> {p['Skill Level']}</li>
        <li><strong># of Projects: </strong> {p['# of Projects']}</li>
        <li><strong>Season: </strong> {p['Season']}</li>
      </ul>
    </div>
    <div class="digital-fine-details">
      <ul>
        <li><strong> Finished Measurements:</strong> {p['Finished Measurements']}</li>
        <li><strong> Yarn Requirements: </strong> {p['Yarn Requirements']}</li>
        <li><strong> Needles and Other Materials </strong> {p['Needles and Other Materials']}</li>
        <li><strong> Gauge: </strong> {p['Gauge']}</li>
        <li><strong> Yarn Weight: </strong> {p['Yarn Weight']}</li>
        <li><strong> Fiber Content: </strong> {p['Fiber Content']}</li>
      </ul>
    </div>
            """

            html_file.write(template)


if __name__ == "__main__":
    parser_obj = ParsingScript()
    parser_obj.parse_csv_to_html()
