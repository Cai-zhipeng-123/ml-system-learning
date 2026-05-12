"""Minimal runnable demo for Spatio-temporal Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "时空学习",
        "english_name": "Spatio-temporal Learning",
        "core_idea": "联合建模空间与时间依赖",
        "typical_tasks": "交通预测、气象预测",
        "representative_algorithms": "STGCN、Temporal Transformer",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
