<template>
	<view class="login-container">
		<view class="avatar-container">
			<image class="avatar" src="https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/logo.png">
			</image>
		</view>
		<view class="form-container">
			<uni-forms ref="form" :modelValue="formData" :rules="rules">
				<uni-forms-item label="用户名" name="name">
					<uni-easyinput type="text" v-model="formData.name" placeholder="请输入用户名" />
				</uni-forms-item>
				<uni-forms-item label="密码" name="password">
					<uni-easyinput type="password" v-model="formData.password" placeholder="请输入密码" />
				</uni-forms-item>
			</uni-forms>
			<view class="button-container">
				<button type="primary" class="login-button" @click="submit">登录</button>
			</view>
		</view>
		<view class="link-container">
			<view class="link-item" @click="registered">
				<text class="register-link">还没有账号？点击注册</text>
			</view>
		</view>
	</view>
</template>




<script>
	export default {
		data() {
			return {
				// 表单数据
				formData: {
					name: '',
					password: ''
				},
				rules: {
					// 对name字段进行必填验证
					name: {
						rules: [{
								required: true,
								errorMessage: '请输入用户名',
							}
						]
					},
					// 对password字段进行必填验证
					password: {
						rules: [{
							required: true,
							errorMessage: '请输入密码',
						}]
					}
				}
			}
		},
		onLoad: function (option) {
			if(option.data != null){
				var result = JSON.parse(option.data);
				console.log("传送数值",result);			
				this.formData.name = result.name;
				this.formData.password = result.password;
			}
				
		},
		methods: {
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
			submit() {
				this.$refs.form.validate().then(res => {
					const formData = {
						...this.formData
					}; // 复制表单数据到一个新对象中
					Object.keys(formData).forEach(key => {
						formData[key] = formData[key].trim(); // 预处理表单数据，去除首尾空格
					});
					// console.log('表单数据信息：', res);

					// const db = uniCloud.database(); // 创建数据库连接
					// db.collection("user").get().then(res => {
					// 	const userData = res.result.data;
					// 	// console.log('用户信息', userData);
					// 	var data = JSON.stringify(userData);
					// 	const isLoggedIn = userData.some(user => {
					// 		return user.name === formData.name && user.password === formData
					// 			.password;
					// 	});
						
					// 	if (isLoggedIn) {

					// 	} else {
					// 	}
					// }).catch(err => {
					// 	console.log(err);
					// });
					
					const db = uniCloud.database(); // 创建数据库连接
					db.collection("user").where({name: formData.name}).get().then(res =>{
						const userData = res.result.data;					
						const isLoggedIn = userData.some(user => {
								return user.password === formData  //比较密码是否相同
									.password;
						})
						if (isLoggedIn) {
							    const data = JSON.stringify(userData)
								//设置全局变量
								getApp().globalData.loginname = userData[0].name   //全局用户名
								getApp().globalData.loginavatar = userData[0].avatar  //全局用户头像
								getApp().globalData.loginstatus = 1  //登录状态
								getApp().globalData.loginid = userData[0]._id  //用户唯一id
								// console.log(getApp().globalData.loginstatus)
								uni.showToast({
									title: '登录成功',
									duration: 1000,
								})
								console.log("data",data)
								setTimeout(function() {
									uni.reLaunch({
										url: '../tabbar/user/user?data='+data
									})
									
								}, 1000);
						
							} else {
								console.log('登录失败');
								uni.showToast({
									title: '用户名或者密码错误',
									icon: 'error'
								})
							}
						
					})
					
					
				}).catch(err => {
					console.log('表单错误信息：', err);
				});
			},
			registered() {
				uni.navigateTo({
					url: '/pages/registered/registered',
				});
			},
			forget() {
				uni.navigateTo({
					url: '/pages/registered/registered',
				});
			}
		}
	}
</script>

<style scoped>
	.login-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
	}

	.avatar-container {
		margin-bottom: 10px;
	}

	.avatar {
		width: 80px;
		height: 80px;
		border-radius: 50%;
	}

	.form-container {
		background-color: #fff;
		padding: 30rpx;
		width: 300px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.button-container {
		display: flex;
		justify-content: center;
		margin-top: 30px;
	}

	.login-button {
		width: 50%;
		height: 40px;
		border-radius: 20px;
		font-size: 16px;
	}

	.link-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-top: 20px;
	}

	.link-item {
		margin-bottom: 10px;
	}

</style>