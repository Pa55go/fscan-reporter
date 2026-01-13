import sys
from parser import parse_fscan_result
from reporter import generate_markdown, generate_word


def main():
    input_file = "result.txt"  # 你的 fscan 输出文件

    print(f"[*] 正在解析 fscan 结果: {input_file}")
    data = parse_fscan_result(input_file)

    print("[*] 正在生成 Markdown 报告...")
    generate_markdown(data, "output/report.md")

    print("[*] 正在生成 Word 报告...")
    generate_word(data, "output/report.docx")

    print("[+] 报告生成成功！存放于 output 目录下。")


if __name__ == "__main__":
    main()