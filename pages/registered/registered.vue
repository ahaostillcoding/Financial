<template>
	<view class="uni-padding-wrap">
		<view class="avatar-container" @click.capture="select">
			<image class="avatar" :src="selectedAvatar">
			</image>
			<view class="avatar-label">
				<text>选择头像</text>
			</view>
		</view>
		<view class="form-container">
			<uni-forms ref="form" :modelValue="formData" :rules="rules">
				<uni-forms-item label="用户名" name="name">
					<uni-easyinput type="text" v-model="formData.name" placeholder="请输入用户名" />
				</uni-forms-item>
				<uni-forms-item label="密码" name="password">
					<uni-easyinput type="password" v-model="formData.password" placeholder="请输入密码" />
				</uni-forms-item>
				<uni-forms-item label="确认密码" name="ConfirmPassword">
					<uni-easyinput type="password" v-model="formData.ConfirmPassword" placeholder="请确认密码" />
				</uni-forms-item>
				<button type="primary" class="register-button" @click="registered">注册</button>
			</uni-forms>
		</view>


		<!-- 头像弹窗 -->
		<uni-popup class="popup-content" ref="popup" :mask-click="true" background-color="#fff">
			<view>
				<div style="text-align: right; margin: 10px 15px 0px 0;">
					<img src="https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/close.png"
						@click="close" style="width: 20rpx; text-align: right;" />
				</div>
				<view class="avatar-text">
					<text>请选择一个头像</text>
				</view>

				<view class="image-content">
					<uni-grid class="image-container" :column="4" :highlight="true" :square="false" @change="change"
						:showBorder="false">
						<uni-grid-item v-for="(item, index) in taglist" :index="index" :key="index">
							<view class="image-wrapper">
								<image :src="item.url" class="image" mode="aspectFill" />
								<text class="text">{{ item.text }}</text>
							</view>
						</uni-grid-item>
					</uni-grid>
				</view>
			</view>
		</uni-popup>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 表单数据
				formData: {
					name: '',
					password: '',
					ConfirmPassword: '',
				},

				selectedAvatar: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/NOTION_AVATAR (1).png', //选择的头像url

				taglist: [{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/NOTION_AVATAR (1).png',

					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/NOTION_AVATAR (2).png',

					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/NOTION_AVATAR (3).png',

					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/NOTION_AVATAR (4).png',

					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/NOTION_AVATAR (5).png',

					},
					{
						url: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/NOTION_AVATAR (6).png'
					}
				],
				rules: {
					// 对name字段进行必填验证
					name: {
						rules: [{
								required: true,
								errorMessage: '请输入用户名',
							},
							{
								minLength: 2,
								maxLength: 8,
								errorMessage: '姓名长度在 {minLength} 到 {maxLength} 个字符',
							},
						],
					},
					// 对password字段进行必填验证
					password: {
						rules: [{
								required: true,
								errorMessage: '请输入密码',
							},
							{
								minLength: 5,
								maxLength: 20,
								errorMessage: '密码长度在 {minLength} 到 {maxLength} 个字符',
							},
						],
					},
					ConfirmPassword: {
						rules: [{
								required: true,
								errorMessage: '请输入确认密码',
							},
							{
								validateFunction: function(rule, value, data, callback) {
									if (value != data.formData.password) {
										callback(data.formData)
									}
									return true
								}
							},
						],
					},
				},
			};
		},
		methods: {
			/**
			 * 触发提交表单
			 */
			registered() {
				this.$refs.form.validate().then((res) => {

					// console.log('表单数据信息：', res);
					let data = {
						name: res.name,
						password: res.password,
						avatar: this.selectedAvatar
					}
					// uni.showLoading({
					// 	title: '加载中'
					// });

					// setTimeout(function () {
					// 	uni.hideLoading();
					// }, 500);
					var result = JSON.stringify(data);
					console.log('用户信息', result);
					const db = uniCloud.database() //创建数据库连接
					db.collection("user").where({
						name: res.name
					}).get().then(res => {
						const userData = res.result.data;
						// console.log("res",userData)
						if (userData.length === 0) {
							db.collection("user").add(data) //获取数据表的信息
								.then(res => {
									console.log('注册成功', res)
									uni.showToast({
										title: '注册成功'
									})
									setTimeout(function() {
										uni.redirectTo({
											url: '../login/login?data=' + result
										})
									}, 1000);
								})
								.catch(err => {
									console.log(err)
								})
							// console.log('可以注册')
						} else {
							uni.showToast({
								title: '用户名已注册',
								icon: 'error'
							})
							this.formData.name = '';
						}
					})


				}).catch((err) => {
					console.log('表单错误信息：', err);
				});
			},
			/**
			 * 自定义验证函数，用于验证两次密码是否一致
			 */
			validateConfirmPassword(value, formData) {
				if (value !== formData.password) {
					return {
						valid: false,
						message: '两次密码不一致',
					};
				}
				return {
					valid: true,
				};
			},

			select() {
				console.log("选择头像")
				this.$refs.popup.open('center')
			},

			close() {
				this.$refs.popup.close()
			},

			change(e) {
				let {
					index
				} = e.detail
				const selectedAvatar = this.taglist[index].url;
				console.log(selectedAvatar)
				this.selectedAvatar = selectedAvatar
				this.close()
			},

		},
	};
</script>

<style scoped>
	.uni-padding-wrap {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
	}

	.avatar-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-bottom: 20px;
	}

	.avatar {
		width: 60px;
		height: 60px;
		border-radius: 50%;
	}

	.image {
		width: 40px;
		height: 40px;
		/* margin: 30px; */
	}

	.image-content {
		height: 400upx;
		width: 500upx;
	}

	.image-container {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		margin-left: 25upx;
		margin-right: 10upx;
		margin-top: 30upx;
	}

	.image-wrapper {
		display: flex;
		flex-direction: column;
		align-items: center;
		/* margin: 10px; */
		margin-right: auto;

	}

	.image {
		width: 80px;
		height: 80px;
	}

	.text {
		margin-top: 10px;
		font-size: 14px;
		color: #666;
		text-align: center;
	}

	.avatar-label {
		margin-top: 10px;
		font-size: 14px;
		opacity: 0.6;
		color: #666;
	}

	.avatar-text {
		text-align: center;
		font-size: 18px;
		margin-bottom: 5px;
	}

	.form-container {
		background-color: #fff;
		padding: 30rpx;
		width: 300px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.grid-content {
		display: flex;
		flex-direction: column;
	}

	.popup-content {
		height: 450upx;
		width: 600upx;
	}

	.register-button {
		width: 50%;
		height: 40px;
		margin-top: 10px;
		border-radius: 20px;
		font-size: 16px;
	}
</style>