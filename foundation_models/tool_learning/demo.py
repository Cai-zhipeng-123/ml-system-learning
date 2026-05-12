"""Minimal runnable demo for Tool Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "Tool Learning",
        "english_name": "Tool Learning",
        "core_idea": "学习调用外部工具解决任务",
        "typical_tasks": "搜索、代码执行、API 调用",
        "representative_algorithms": "Toolformer",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
