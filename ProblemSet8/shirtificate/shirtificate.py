from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", size=45)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.ln(120)
    def body(self, name):
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", size=30)
        self.cell(0, None, f"{name} took CS50", align="C", center="True")



def main():
    pdf = PDF()
    pdf.add_page()
    pdf.image(
        name="shirtificate.png",
        x=5,
        y=70,                      # 距页面顶部 70 单位
        w=pdf.epw,                 # Effective page width: the page width minus its horizontal margins.
        keep_aspect_ratio=True,
    )
    pdf.body(input("Name: "))

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
