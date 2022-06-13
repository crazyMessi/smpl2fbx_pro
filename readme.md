基于[SMPL2FBX](https://github.com/softcat477/SMPL-to-FBX)

增加了:

* 骨骼动作的平滑拼接
* 一些其他小功能



总结将模型a的动画迁移到b要做的事情:

* 弄一个骨骼关节的映射
* 在maya里面调整b的关节朝向 要与a一致 例如smpl里面的都是世界坐标系
