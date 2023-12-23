<template>
	<view class="content">
		<uni-forms class="forms" ref="form" :modelValue="formData" :rules="rules">
			<uni-forms-item label="金额:" name="money">
				<uni-easyinput type="digit" v-model="formData.money" placeholder="请输入收入金额" />
			</uni-forms-item>
			<uni-forms-item label="时间:" name="datetime">
				<!-- <uni-easyinput v-model="formData.time" placeholder="请输入支出金额" /> -->
				<view class="example-body">
					<uni-datetime-picker type="datetime" v-model="formData.datetime" @change="changeLog" />
				</view>			
			</uni-forms-item>
			<uni-forms-item label="标签:" name="tag">
				<uni-easyinput suffixIcon="search" type="text" v-model="formData.tag" @iconClick="addTag()" placeholder="请添加标签" />						
			</uni-forms-item>
			<uni-forms-item label="备注:" name="remark">
				<uni-easyinput type="text" v-model="formData.remark" placeholder="请添加备注" />						
			</uni-forms-item>
			
			<!-- 标签弹窗 -->
			<uni-popup ref="popup" :mask-click="true" background-color="#fff">
				<view>						
					<div style="text-align: right; margin: 10px 15px 0px 0;">
						<img src="https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/close.png" @click="close" style="width: 20rpx; text-align: right;" />
					</div>
					<text>请选择一个标签</text>
					
					<uni-grid :column="3" :highlight="true" :square="false" @change="change" :showBorder="false">
					  <uni-grid-item v-for="(item, index) in taglist" :index="index" :key="index">
					    <view class="grid-item-box">
					      <image :src="item.url" class="image" mode="aspectFill" />
					      <text class="text">{{ item.text }}</text>
					    </view>
					  </uni-grid-item>
					</uni-grid>
				</view>
			</uni-popup>
			
		</uni-forms>
		<view >
			<div>
				<button @click="update" type="primary">修改</button>
				<button @click="remove" type="warn">删除</button>
				<button @click="cancel" type="default">取消</button>
			</div>
			
		</view>
	
	</view>
</template>

<script>
	export default {
		data() {
			return {
				tagUrl: '',  //标签图标
				id: '', //每个数据的唯一标识
				// 表单数据
				formData: {
					money: '',
					tag: '',
				    remark: '',
					datetime: '' 
				},
				rules: {
					money: {
						rules: [{
								required: true,
								errorMessage: '请输入收入金额',
							}
						]
					},
					// 对email字段进行必填验证
					tag: {
						rules: [{
							// required: true,
							// errorMessage: '请添加标签',
						}]
					}
				},
				taglist: [{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/food.png',
						text: '餐饮',
					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/shop.png',
						text: '购物',
					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/bus.png',
						text: '交通',
					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/study.png',
						text: '学习',
					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/doctor.png',
						text: '医疗'
					}
				]
			}
		},
		onLoad: function (option) {
				var result = JSON.parse(option.data);
				// console.log("传送数值",result);
				
				// 用于显示传递内容
				this.formData.money = result.money;
				this.formData.tag = result.tag;
				this.formData.datetime = result.datetime;
				this.tagUrl = result.tagUrl;
				this.formData.remark = result.remark;
				this.$forceUpdate();
				
				//用于寻找对应数据库的中表
				this.id = result.id;  
		},
		// onLoad() {
		// 	this.getStatus()
		// },
		methods: {
			getStatus() {
					  console.log("status",getApp().globalData.loginstatus)
					  if(getApp().globalData.loginstatus == false){
						  uni.reLaunch({
						  	url: '/pages/login/login'
						  })
					  }
			},
			/**
			 * 复写 binddata 方法，如果只是为了校验，无复杂自定义操作，可忽略此方法
			 * @param {String} name 字段名称
			 * @param {String} value 表单域的值
			 */
			// binddata(name,value){
			// 通过 input 事件设置表单指定 name 的值
			//   this.$refs.form.setValue(name, value)
			// },
			// 触发提交表单			
			update() {
				this.$refs.form.validate().then(res=>{
					console.log('表单数据信息：', res);
				}).catch(err =>{
					console.log('表单错误信息：', err);
				})
				//添加表单数据到数据库
				let data = {
					money: this.formData.money,
					datetime: this.formData.datetime,
					tagUrl: this.tagUrl,
					tag: this.formData.tag,
					remark: this.formData.remark
				}
				console.log(data)
				
				const db = uniCloud.database()//创建数据库连接
				db.collection("output").doc(this.id).update(data)//获取数据表的信息
				.then(res => {
					console.log(res,'修改数据成功')
					uni.showToast({
						title: '修改数据成功',
						duration: 1000,
					})
					setTimeout(function () {
						uni.reLaunch({
							url: '../../tabbar/detail/detail'
						})
					}, 1200);
				})
				.catch(err => {
					console.log(err)
				})
			},
			remove() {
				const db = uniCloud.database()//创建数据库连接
				db.collection("output").doc(this.id).remove()
				.then(res => {
					uni.showToast({
						title: '删除数据成功',
						duration: 1000,
					})
					setTimeout(function () {
						uni.reLaunch({
							url: '../../tabbar/detail/detail'
						})
					}, 1200);
				})
				.catch(err => {
					console.log(err)
				})
			},
			cancel() {
				this.redirect();
			},
			redirect() {
				uni.reLaunch({
					url: '../../tabbar/detail/detail'
				});
			},
			addTag() {
				this.$refs.popup.open('center')
			},
			close() {
				this.$refs.popup.close()
			},
			change(e) {
				let {
					index
				} = e.detail
				const selectedTag = this.taglist[index].text;
				console.log(selectedTag)
				// 改变标签框的值
				this.formData.tag = selectedTag;
				
				// 改变标签图标
				const tagUrl = this.taglist[index].url;
				this.tagUrl = tagUrl;
				console.log(tagUrl)
				
				
				//uni-forms采用的是数据绑定方式更新表单值，不会立马更新值，需要强制刷新表单(坑了我好久)
				this.$forceUpdate();
				this.$refs.popup.close()
			},
			// 时间选择时触发
			changeLog(e) {
				console.log('change事件:', e);
			},

		}
	};
</script>

<style src="" >
	.content {
		text-align: center;
		height: 400upx;
		margin: 50upx 50upx 0 50upx;
	}
	button {
			width: 150px;
			margin: 20px auto;
		}
	
	.forms {
		width: 300px;
	}
	
	.image {
			width: 25px;
			height: 25px;
		}
	
	.text {
		font-size: 14px;
		margin-top: 5px;
	}
	
	.example-body {
		/* #ifndef APP-NVUE */
		// display: block;
		/* #endif */
	}
	
	.grid-dynamic-box {
		margin-bottom: 15px;
	}
	
	.grid-item-box {
		flex: 1;
		// position: relative;
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 15px 0;
	}
	
	.grid-item-box-row {
		flex: 1;
		// position: relative;
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		align-items: center;
		justify-content: center;
		padding: 15px 0;
	}
	
	.grid-dot {
		position: absolute;
		top: 5px;
		right: 15px;
	}
	
	.swiper {
		height: 420px;
	}
	
	/* #ifdef H5 */
	@media screen and (min-width: 768px) and (max-width: 1425px) {
		.swiper {
			height: 630px;
		}
	}
	
	@media screen and (min-width: 1425px) {
		.swiper {
			height: 830px;
		}
	}
	
	/* #endif */
	
</style>
