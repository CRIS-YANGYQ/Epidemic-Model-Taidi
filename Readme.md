## Readme.md
- 该项目是面向2023年第十一届“泰迪杯”数据挖掘挑战赛A题的解决方案
### Codes
* 所有程序源码保存在Codes文件目录下，其中包含了 " Q1&Q2 ", " Q3&Q4 " 和 " Q5 "三个文件夹。
  * 第一、二问的源代码在 " Q1&Q2 " 文件下的 " codes " 文件夹，包括了问题解决源码、数据可视化和数据库建立的python文件。'' images " 文件夹中包含了可视化的输出图例（***.png）
  * 第三、四问的源代码在 " Q3&Q4 " 文件夹内，其中包含用于 jupyter notebook markdown部分所使用的图例（***.png）和 " img " 文件夹。" img " 文件夹中存放了代码中模型输出和数据可视化的图例 。
  * 第五问的源代码保存在 " Q5 " 文件夹内，包含一个 jupyter notebook。
* 为减少程序压缩包大小，一二问的结果文件  "  result1.csv " 和 "result2.csv " 已通过网站单独提交，不再放入此压缩包中。

### Final——Papers
* 包含最终论文
### Reference
* 引用论文
### Request_book
* 赛题要求
## Abstract
从新冠疫情最初的爆发，到如今的疫情常态化，全国各地陆续出现了不同程度的新冠病毒感染情况。疫情数据是反映各地疫情形势的重要信息来源，主要包括人员信息、场所信息、个人自查上报信息、场所扫码信息、核酸采样检测信息、疫苗接种信息等。通过分析这些数据，能协助我们有效实行疫情精准防控，有利于进行人员分类管理、传播途径追踪、疫情追溯、控制疫情蔓延等。因此本文围绕疫情数据，运用 MySQL 数据库实现人员分类管理，并结合 SIR 等传染病传播模型，实现对接种疫苗对病毒传播指数影响的分析。同时，尝试利用 DBSCAN 等聚类方法以及尝试调整损失函数对不同风险场所进行分类运用 DBSCAN 和进行流行病学特征分析，结合格兰杰因果检验，对疫情的精准防控进行进一步优化。主要研究内容和成果包括以下几部分
- 一、人员分类管理：首先基于赛题附件所给的表格，设计 E-R 图，创建数据库；然后从时间和空间两个维度，追踪阳性个体的出行轨迹，以识别可能存在的时空伴随者，后依照国务院发布的《新型冠状病毒肺炎防控方案（第九版）》（下称防控九版）判断密接者；其次，得到密接者信息后，以防控九版中次密接者识别的方法，可进一步识别次密接者。
- 二、接种疫苗对病毒传播影响分析：首先依据核酸采样检测信息表和疫苗接种信息表等得出接种过疫苗的人中核酸阳性的概率及每日累计确诊人数；其次，采用优化算法，基于总体人口和接种疫苗者的感染数据，对 SIR 模型中的传染率进行参数判别，得出传染率μ和恢复率γ；然后引入 SEIR 模型和 SEIDR 模型，并考虑接种疫苗因素修改原有数学模型，分别得出无疫苗情况和接种不同针数疫苗的情况下易感者、暴露者/潜伏者、感染者、死亡者和康复者人数随时间的变化趋势，基于已有数据建立仿真建模；最后计算各个时间基本再生数，对比未接种疫苗和接种疫苗情况下基本再生数 $R_0$ 的大小和变化趋势，以此量化分析接种疫苗对病毒传播的影响。
- 三、重点管控场所的分析确定：首先，通过确定各场所人流量及阳性人员流动量，建立特征；其次运用 DBSCAN 和损失函数进行聚类分析，进而得到各场所病例的分布，划分高中低风险区，为地方政府科学地划分疫情风险等级，明确分级分类的防控策略提供科学依据；最后考虑时间序列分析，使用格兰杰因果检验，对中高风险区进行两两因果检验，据此分析两个区域疫情爆发有无因果关系，分析区域疫情的空间传播性。
- 四、实现精准防控：为实现精准防控和人员管理，除了附件中的疫情数据，还需要采集一个城市人员的流入和流出信息；通过采集到的数据，计算扩散比（DR）和人口流动比率（MR）；构建目标城市各点坐标的邻接矩阵，采用Moran系数和 Geary 系数进行全域空间相关性检验，并进行局部自相关性检验，以此弥补整体检验对局部特征的敏感程度；最后利用加权法可以算出某一地点在某特定时间段传播风险指数。
