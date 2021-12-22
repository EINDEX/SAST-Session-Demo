import subprocess

def fake_escape(content):
    return content.replace("a", "b")

def escape(content):
    return content.replace("<", "&lt;").replace(">", "&gt;")