def regexer():
    import json
    import re
    file_path = 'DataFiles/RawData/myJson.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
        sha1_hashes = re.findall(r'(?i)([a-f\d]{40})', json.dumps(data))
        sha256_hashes = re.findall(r'(?i)([a-f\d]{64})', json.dumps(data))
        domains = re.findall(r'(?i)([a-z0-9]+\.[a-z]{2,})', json.dumps(data))
        ipv4 = re.findall(r'(?i)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', json.dumps(data))
        csver(ipv4, sha1_hashes, sha256_hashes, domains)
        csver(ipv4,sha1_hashes,sha256_hashes,domains)
        return ipv4,sha1_hashes,sha256_hashes,domains


def csver(ipv4,sha1_hashes,sha256_hashes,domains):
    import csv
    with open("iocs.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Type", "Value"])
        for sha1 in sha1_hashes:
            writer.writerow(["SHA1", sha1])
        for sha256 in sha256_hashes:
            writer.writerow(["SHA256", sha256])
        for domain in domains:
            writer.writerow(["Domain", domain])
        for ip in ipv4:
            writer.writerow(["IPv4", ip])




