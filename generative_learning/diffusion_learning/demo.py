"""Minimal runnable demo for Diffusion Learning.

This file intentionally keeps the code small. Replace the placeholder
logic with a real experiment when studying this topic.
"""


def describe() -> dict[str, str]:
    return {
        "name": "扩散生成学习",
        "english_name": "Diffusion Learning",
        "core_idea": "学习逐步去噪恢复数据分布",
        "typical_tasks": "AI 绘画、视频生成、AIGC",
        "representative_algorithms": "DDPM、Stable Diffusion",
    }


def main() -> None:
    info = describe()
    print(f"Learning paradigm: {info['name']} ({info['english_name']})")
    print(f"Core idea: {info['core_idea']}")
    print(f"Typical tasks: {info['typical_tasks']}")
    print(f"Representative algorithms: {info['representative_algorithms']}")


if __name__ == "__main__":
    main()
