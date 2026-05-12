# 机器学习框架总览

本文档用于构建机器学习算法学习项目，按照学习范式将机器学习体系划分为六大模块：判别式学习、生成式学习、交互式学习、迁移与泛化学习、结构化学习、现代基础模型。

---

## 一、判别式学习（Discriminative Learning）

判别式学习关注学习：

$$
P(Y \mid X) \quad \text{或} \quad f: X \rightarrow Y
$$

即：

- 从输入预测输出
- 建模“决策边界”
- 强调预测能力

| 学习范式 | 核心思想 | 典型任务 | 代表算法/模型 |
|---|---|---|---|
| 监督学习<br>Supervised Learning | 利用标签数据学习输入到输出映射 | 分类、回归、排序、序列预测、结构化预测 | LR、SVM、XGBoost、CNN、Transformer |
| 半监督学习<br>Semi-supervised Learning | 利用少量标签与大量无标签联合训练 | 图像分类、文本分类、目标检测、医学影像 | Pseudo-Label、FixMatch、Label Propagation |
| 自监督学习<br>Self-supervised Learning | 从数据自身构造监督信号学习表征 | 预训练、表示学习、跨模态对齐、Embedding 学习 | BERT、SimCLR、MAE、MoCo |
| 多任务学习<br>Multi-task Learning | 多个相关任务共享表示并联合优化 | CTR+CVR 预测、多目标推荐、多头预测 | Shared-Bottom、MMoE |
| 在线学习<br>Online Learning | 数据流式到达时持续更新模型 | CTR 预估、实时推荐、股票预测、风控 | Online SGD、FTRL |
| 对比学习<br>Contrastive Learning | 拉近正样本、拉远负样本学习表示 | 检索、Embedding 学习、推荐、视觉预训练 | SimCLR、MoCo、InfoNCE |
| 排序学习<br>Learning to Rank | 直接优化样本排序关系 | 搜索排序、广告排序、推荐排序 | RankNet、LambdaMART |
| 度量学习<br>Metric Learning | 学习距离空间中的相似性度量 | 人脸识别、向量检索、商品匹配 | Triplet Loss、Siamese Network |
| 结构化预测<br>Structured Prediction | 预测具有结构依赖的输出 | NLP 序列标注、语法分析、OCR | CRF、Seq2Seq、Transformer |
| 异常检测<br>Anomaly Detection | 学习正常模式识别异常样本 | 欺诈检测、设备故障、网络安全 | Isolation Forest、One-Class SVM |

---

## 二、生成式学习（Generative Learning）

生成式学习关注学习数据分布：

$$
P(X) \quad \text{或} \quad P(X, Y)
$$

进而：

- 生成新样本
- 建模世界分布
- 学习潜在表示

| 学习范式 | 核心思想 | 典型任务 | 代表算法/模型 |
|---|---|---|---|
| 概率生成学习<br>Probabilistic Generative | 建模数据概率分布生成样本 | 密度估计、生成建模 | GMM、HMM |
| 自回归生成<br>Autoregressive Modeling | 按条件概率逐步生成序列 | 文本生成、代码生成、语音生成 | GPT、PixelRNN |
| 变分生成学习<br>Variational Learning | 学习潜在变量概率分布 | 图像生成、表征学习、降维 | VAE、CVAE |
| 对抗生成学习<br>Adversarial Learning | 生成器与判别器对抗训练 | 图像生成、风格迁移、超分辨率 | GAN、StyleGAN |
| 扩散生成学习<br>Diffusion Learning | 学习逐步去噪恢复数据分布 | AI 绘画、视频生成、AIGC | DDPM、Stable Diffusion |
| 掩码生成学习<br>Masked Modeling | 预测被遮蔽部分恢复原数据 | NLP 预训练、视觉预训练 | BERT、MAE |
| 能量模型<br>Energy-based Learning | 用能量函数刻画数据分布 | 密度估计、联想记忆 | RBM、Hopfield Network |
| 世界模型<br>World Model | 学习环境动态与状态转移 | Agent、机器人、规划 | Dreamer、MuZero |
| 多模态生成<br>Multimodal Generation | 联合建模多模态数据分布 | 图文生成、视频理解、Agent | CLIP、Flamingo、GPT-4o |

---

## 三、交互式学习（Interactive Learning）

交互式学习强调模型通过：

- 环境反馈
- 人类反馈
- 主动交互

持续优化策略。

| 学习范式 | 核心思想 | 典型任务 | 代表算法/模型 |
|---|---|---|---|
| 强化学习<br>Reinforcement Learning | 与环境交互最大化长期奖励 | 游戏 AI、机器人、推荐、调度 | DQN、PPO、A3C |
| 模仿学习<br>Imitation Learning | 模仿专家行为学习策略 | 自动驾驶、机器人控制 | Behavior Cloning、GAIL |
| 主动学习<br>Active Learning | 主动选择最有价值样本标注 | 数据标注、人机协同学习 | Uncertainty Sampling、QBC |
| 人类反馈学习<br>RLHF | 利用人类偏好优化模型行为 | 大模型对齐、Agent | PPO、DPO |
| 赌博机学习<br>Bandit Learning | 在探索与利用间动态权衡 | 广告推荐、实验优化 | UCB、Thompson Sampling |
| 逆强化学习<br>Inverse RL | 从行为反推奖励函数 | 自动驾驶、机器人规划 | MaxEnt IRL |

---

## 四、迁移与泛化学习（Transfer & Generalization）

迁移与泛化学习的目标是提升模型：

- 泛化能力
- 少样本适应能力
- 跨领域迁移能力

| 学习范式 | 核心思想 | 典型任务 | 代表算法/模型 |
|---|---|---|---|
| 迁移学习<br>Transfer Learning | 将源任务知识迁移到目标任务 | 小样本学习、领域迁移 | Fine-tuning、Domain Adaptation |
| 元学习<br>Meta Learning | 学习如何快速适应新任务 | Few-shot Learning、NAS | MAML、ProtoNet |
| 持续学习<br>Continual Learning | 连续学习多个任务避免遗忘 | 增量学习、终身学习 | EWC、Replay |
| 领域泛化<br>Domain Generalization | 学习跨域稳定特征 | 跨设备、跨场景学习 | IRM、MetaDG |
| 小样本学习<br>Few-shot Learning | 用极少样本完成新任务 | 小样本分类、医学 AI | ProtoNet、MatchingNet |
| 零样本学习<br>Zero-shot Learning | 不见样本直接泛化到新类别 | 开集识别、多模态推理 | CLIP、Instruction Tuning |
| 参数高效迁移<br>PEFT | 少量参数完成迁移 | 大模型微调 | LoRA、Adapter |
| 联邦学习<br>Federated Learning | 分布式隐私保护协同训练 | 医疗、金融建模 | FedAvg、FedProx |

---

## 五、结构化学习（Structured Learning）

结构化学习利用：

- 图结构
- 概率依赖
- 因果关系
- 时空关系

建模复杂世界。

| 学习范式 | 核心思想 | 典型任务 | 代表算法/模型 |
|---|---|---|---|
| 图学习<br>Graph Learning | 利用图结构传播节点关系 | 推荐、社交网络、知识图谱 | GCN、GAT、GraphSAGE |
| 图表示学习<br>Graph Embedding | 学习节点/图低维表示 | 节点分类、链路预测 | DeepWalk、Node2Vec |
| 概率图模型<br>Probabilistic Graph | 用图表示随机变量依赖关系 | 推断、诊断、时序建模 | Bayesian Network、Markov Random Field |
| 贝叶斯学习<br>Bayesian Learning | 基于后验概率更新知识 | 不确定性建模、小样本学习 | Bayesian Regression、GP |
| 因果学习<br>Causal Learning | 学习变量间因果关系 | 因果推断、策略评估 | DAG、DID、IV、RDD |
| 时空学习<br>Spatio-temporal Learning | 联合建模空间与时间依赖 | 交通预测、气象预测 | STGCN、Temporal Transformer |
| 序列建模<br>Sequential Learning | 建模时间顺序依赖 | NLP、语音、时间序列 | LSTM、Transformer |
| 关系学习<br>Relational Learning | 学习实体与关系交互 | 知识图谱推理 | TransE、RotatE |

---

## 六、现代基础模型（Foundation Models）

基础模型的核心特征包括：

- 大规模预训练
- 通用表示学习
- 跨任务泛化
- 多模态统一

| 学习范式 | 核心思想 | 典型任务 | 代表算法/模型 |
|---|---|---|---|
| 大语言模型<br>LLM | 基于海量文本学习通用语言能力 | 对话、推理、代码生成 | GPT、Llama、DeepSeek |
| 视觉基础模型<br>Vision Foundation Model | 大规模视觉预训练 | 图像分类、检测、分割 | ViT、SAM |
| 多模态基础模型<br>Multimodal Foundation Model | 联合建模文本、图像、语音 | Agent、视觉问答、视频理解 | GPT-4o、Gemini |
| Agent Learning | 基于工具调用与规划执行任务 | 自动 Agent、工作流自动化 | ReAct、AutoGPT |
| Tool Learning | 学习调用外部工具解决任务 | 搜索、代码执行、API 调用 | Toolformer |
| 检索增强学习<br>RAG | 结合外部知识增强生成 | 企业知识库、问答系统 | DPR、RAG |
| 世界模型<br>World Foundation Model | 学习世界动态规律与规划 | 机器人、自动驾驶 | MuZero、Dreamer |
| 长上下文学习<br>Long-context Learning | 处理超长序列与记忆 | 长文推理、代码库分析 | Transformer-XL、Longformer |
