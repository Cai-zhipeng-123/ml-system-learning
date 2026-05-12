# ML System Learning

这是一个面向机器学习算法体系化学习的 Python 项目。项目根据 `machine_learning_framework.md` 中的框架，将机器学习学习路径拆成六大模块，并在每个学习范式下准备理论笔记、最小示例和实验 notebook 占位。

## 项目目标

- 建立清晰、可扩展的机器学习算法学习目录。
- 以最小可运行示例起步，逐步补充真实算法实现。
- 将理论、实验、代码和学习记录放在同一套结构中持续迭代。

## 学习路线

1. 先学习判别式学习，建立分类、回归、排序和表示学习的基础。
2. 再学习生成式学习，理解概率分布、潜变量、对抗训练和扩散建模。
3. 继续学习交互式学习，掌握环境反馈、人类反馈和探索利用权衡。
4. 补充迁移与泛化学习，面向小样本、跨域、持续学习和高效微调。
5. 深入结构化学习，理解图、贝叶斯、因果、时空和关系建模。
6. 最后进入现代基础模型，连接 LLM、多模态、RAG、Agent 和长上下文学习。

## 模块总览

| 模块 | 英文 | 范式数量 | 说明 |
|---|---:|---:|---|
| [判别式学习](./discriminative_learning/) | Discriminative Learning | 10 | 关注从输入到输出的映射，学习决策边界或条件概率 P(Y|X)。 |
| [生成式学习](./generative_learning/) | Generative Learning | 9 | 关注建模数据分布 P(X) 或联合分布 P(X,Y)，用于生成、补全和表征学习。 |
| [交互式学习](./interactive_learning/) | Interactive Learning | 6 | 通过环境反馈、人类反馈或主动交互持续优化策略。 |
| [迁移与泛化学习](./transfer_and_generalization/) | Transfer & Generalization | 8 | 提升模型泛化、少样本适应和跨领域迁移能力。 |
| [结构化学习](./structured_learning/) | Structured Learning | 8 | 利用图结构、概率依赖、因果关系和时空关系建模复杂世界。 |
| [现代基础模型](./foundation_models/) | Foundation Models | 8 | 面向大规模预训练、通用表示学习、跨任务泛化和多模态统一。 |

## 目录结构

```text
ml-system-learning/
├── README.md
├── requirements.txt
├── docs/
│   └── machine_learning_framework.md
├── discriminative_learning/
├── generative_learning/
├── interactive_learning/
├── transfer_and_generalization/
├── structured_learning/
├── foundation_models/
```

每个学习范式目录都包含：

- `README.md`：核心思想、典型任务和代表算法。
- `theory.md`：理论笔记占位。
- `demo.py`：最小可运行 Python 示例。
- `notebook.ipynb`：实验 notebook 占位。

## 快速开始

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python discriminative_learning/supervised_learning/demo.py
```
