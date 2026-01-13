# fscan-reporter

## 项目简介

**fscan-reporter** 是一个自动化报告生成工具，专门用于处理 [fscan](https://github.com/shadow1ng/fscan) 网络安全扫描工具的输出结果，并将其转换为结构化的 Markdown 和 Word 报告。

## 功能特性

- **多编码支持**：自动尝试 `utf-8`、`gbk`、`gb18030`、`latin-1` 等多种编码格式解析 fscan 输出文件
- **智能解析**：根据 `[+]` 和 `[*]` 标识符自动分类漏洞和资产信息
- **风险分级**：自动统计严重(Critical)、高危(High)、中危(Medium)、信息(Info)等级别的安全风险
- **双格式输出**：同时生成 Markdown 和 Word 两种格式的专业安全报告
- **可视化图表**：在 Word 报告中嵌入风险分布饼状图
- **自动清理**：处理完成后自动删除临时文件

## 支持的报告格式

- **Markdown (.md)**：适合在线预览和版本控制
- **Word (.docx)**：适合正式提交和打印

## 使用方法

### 前置依赖

```bash
pip install python-docx matplotlib
```


### 运行步骤

1. 将 [fscan](https://github.com/shadow1ng/fscan) 的扫描结果保存为 `report.txt`
2. 将 `report.txt` 放置在脚本同目录下
3. 运行主程序：

```bash
python main.py
```


4. 生成的报告将自动保存到 `output` 目录中

## 输出文件结构

```
output/
├── report.md      # Markdown格式报告
└── report.docx    # Word格式报告
```


## 报告内容

生成的报告包含以下部分：

1. **扫描统计**：风险数量统计和资产信息汇总
2. **漏洞与弱口令详情**：以表格形式展示发现的安全风险
3. **Web资产指纹**：网络资产和服务信息
4. **风险分布图**：可视化展示各类风险占比

## 文件解析规则

- **漏洞识别**：包含 `[+]` 标识的行被识别为安全漏洞
- **资产识别**：包含 `[*]` 标识的行被识别为资产信息
- **风险分级**：根据关键词（如 poc、vuln、ms17-010、rethinkdb）自动分类为严重风险

## 注意事项

- 确保输入文件名为 `report.txt` 或修改 [main.py](file:///E:/project/fscan-reporter/main.py) 中的 [input_file](file:///E:/project/fscan-reporter/main.py#L92-L92) 变量
- 程序会自动创建 `output` 目录用于存放生成的报告
- 支持中文环境下的各种编码格式

## 许可证

MIT License