"""Minimal runnable demo for Sequential Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "序列建模",
        "english_name": "Sequential Learning",
        "core_idea": "建模时间顺序依赖",
        "typical_tasks": "NLP、语音、时间序列",
        "representative_algorithms": "LSTM、Transformer",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
