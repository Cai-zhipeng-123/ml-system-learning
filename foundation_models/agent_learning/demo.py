"""Minimal runnable demo for Agent Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "Agent Learning",
        "english_name": "Agent Learning",
        "core_idea": "基于工具调用与规划执行任务",
        "typical_tasks": "自动 Agent、工作流自动化",
        "representative_algorithms": "ReAct、AutoGPT",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
