from typing import Dict, List

fileIcons: Dict[str, str] = {
    '.txt': '',
    '.py': '',
    '.md': '',
    '.db': '',
    '.gitignore': '',
    '.config': '',
    '.LICENSE': '',
    '.log': '󱦟',
    '.gif': '󰵸',
    '.jpg': '',
    '.png': '',
    '.jpeg': '',
    '.svg': '',
    '.csv': '',
    '.ppt': '󱎐',
    '.pptx': '󱎐',
    '.doc': '󱎒',
    '.docx': '󱎒',
    '.xls': '󱎏',
    '.xlsx': '󱎏',
    '.pdf': '',
    '.mp4': '󰕧',
    '.mkv': '󰕧',
    '.avi': '󰕧',
    '.json': '󰘦',
    '.yaml': '󰭏',
    '.html': ''
}

fileColors: Dict[str, str] = {
    '.txt': '',
    '.py': '',
    '.db': '',
    '.md': '',
    '.gitignore': '[red]',
    '.config': '[cyan]',
    '.LICENSE': '[cyan]',
    '.log': '[blue]',
    '.gif': '[yellow]',
    '.jpg': '[cyan]',
    '.png': '[cyan]',
    '.jpeg': '[cyan]',
    '.svg': '[purple]',
    '.csv': '[green]',
    '.ppt': '[#b7472a]',
    '.pptx': '[#b7472a]',
    '.doc': '[blue]',
    '.docx': '[blue]',
    '.xls': '[green]',
    '.xlsx': '[green]',
    '.pdf': '[red]',
    '.mp4': '',
    '.mkv': '',
    '.avi': '',
    '.json': '',
    '.yaml': '[red]',
    '.html': ''
}

dirIgnore: List[str] = [
    '.git',
    '__pycache__'
]
