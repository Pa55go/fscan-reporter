import re


def parse_fscan_result(file_path):
    results = {
        "vulnerabilities": [],  # 漏洞/弱口令
        "web_titles": [],  # Web指纹
        "net_infos": [],  # 网络信息
        "stats": {"Critical": 0, "High": 0, "Medium": 0, "Info": 0}
    }

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue

            # 简单解析逻辑 (可根据需要增加正则)
            if "[+]" in line:
                results["vulnerabilities"].append(line)
                if any(x in line.lower() for x in ["poc", "vuln", "ms17-010"]):
                    results["stats"]["Critical"] += 1
                else:
                    results["stats"]["High"] += 1
            elif "[*]" in line:
                if "WebTitle" in line:
                    results["web_titles"].append(line)
                else:
                    results["net_infos"].append(line)
                results["stats"]["Info"] += 1

    return results