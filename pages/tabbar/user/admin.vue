<template>
	<view>
		<uni-group mode="card">
			<uni-list class="list">
				<uni-list-item link showArrow clickable @click="avatar">
					<!-- <template v-slot:header>
					<view class="slot-box">
						<image class="slot-image" src="/static/logo.png" mode="widthFix"></image>
					</view>
				</template> -->
					<template v-slot:body>
						<text class="slot-box slot-text">头像</text>
					</template>
					<template v-slot:footer>
						<image class="slot-image" :src="userAvatar" mode="widthFix"></image>
					</template>
				</uni-list-item>

				<uni-list-item link showArrow clickable @click="avatar">
					<template v-slot:body>
						<text class="slot-box slot-text">用户名</text>
					</template>
					<template v-slot:footer>
						<text>{{name}}</text>
					</template>
				</uni-list-item>

				<uni-list-item link showArrow clickable @click="avatar">
					<template v-slot:body>
						<text class="slot-box slot-text">性别</text>
					</template>
					<template v-slot:footer>
						<text>{{sex}}</text>
					</template>
				</uni-list-item>
				
			</uni-list>
		</uni-group>
			
		<uni-group mode="card">
			<uni-list class="list">
				<uni-list-item link showArrow clickable @click="avatar">
					<template v-slot:body>
						<text class="slot-box slot-text">邮箱</text>
					</template>
					<template v-slot:footer>
						<text>邮箱</text>
					</template>
				</uni-list-item>
				
				<uni-list-item link showArrow clickable @click="avatar">
					<template v-slot:body>
						<text class="slot-box slot-text">手机号</text>
					</template>
					<template v-slot:footer>
						<text>手机号</text>
					</template>
				</uni-list-item>
			</uni-list>
		</uni-group>


		<uni-group mode="card">
			<uni-list>
				<uni-list-item @click="removeUser" title="注销账号" note="注销后账号无法找回" link></uni-list-item>
				<uni-list-item @click="changeLogin" title="切换账号" link></uni-list-item>
			</uni-list>
		</uni-group>
		<uni-group >
			<button class="button" @click="unLogin">退出登陆</button>
		</uni-group>
		
		<view>
			<!-- 提示窗 -->
			<uni-popup ref="popup" type="dialog">
				<uni-popup-dialog mode="base" title="注销账号" type="error" content="确认要注销账号吗？" message="成功消息" :duration="2000" :before-close="true" @close="close" @confirm="confirm"></uni-popup-dialog>
			</uni-popup>
		</view>
		<!-- <uni-popup class="popup-content" ref="popup" :mask-click="true" background-color="#fff">
			<view>
				<div style="text-align: right; margin: 10px 15px 0px 0;">
					<img src="https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/close.png"
						@click="close" style="width: 20rpx; text-align: right;" />
				</div>
				<view class="avatar-text">
					<text>更换头像</text>
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
		</uni-popup> -->
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				msgType: '',
				userAvatar: '/static/logo.png',
				name: '用户名',
				sex: '男',
				id: "",
								
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
			}
		},
		onLoad: function (option) {
		  if (option.data != null) {
		    // 解析 JSON 字符串
		    var result = JSON.parse(decodeURIComponent(option.data));
		    console.log("接受数据", result);
		    this.name = result.name;
		    this.userAvatar = result.userAvatar;
			this.id = result.id;
		  } else {
		    console.log("数据为空");
		  }
		},
		onLoad() {
			this.getUser()
			},
		methods: {
			removeUser() {
				this.$refs.popup.open()
			},
			close() {
				this.$refs.popup.close()
			},
			confirm(value) {
				//确认注销
				this.$refs.popup.close()
				// 删除数据库中对应用户名数据
				
				const db = uniCloud.database()//创建数据库连接
				
				db.collection("user").where({_id: getApp().globalData.loginid}).remove()
				.then(res => {
					uni.showToast({
						title: '注销账号成功',
						duration: 1000,
					})
					setTimeout(function () {
						uni.reLaunch({
							url: '/pages/login/login'
						})
					}, 1000);
				})
			},
			changeLogin() {
				setTimeout(function () {
					uni.reLaunch({
						url: '/pages/login/login'
					})
				}, 1000);
			},
			getUser() {
				this.name = getApp().globalData.loginname,
				this.userAvatar = getApp().globalData.loginavatar
				
				
				// #ifdef APP-PLUS
				 uni.startSoterAuthentication({
				 	requestAuthModes: ['fingerPrint'],
				 	challenge: '123456',
				 	authContent: '使用指纹解锁',
				 	success(res) {
				 		console.log("succes",res);
				 	},
				 	fail(err) {
				 		console.log("err",err);
				 	},
				 	complete(res) {
				 		console.log("complete",res);
				 	}
				 })
				 // #endif
			},
			avatar() {
				console.log('点击头像')
				console.log("id",this.id)
			},
			unLogin() {
				getApp().globalData.loginname = ''
				getApp().globalData.loginavatar = ''
				getApp().globalData.loginstatus = 0
				uni.showToast({
					title: '退出登录'
				})
				setTimeout(function() {
					uni.reLaunch({
						url: '/pages/tabbar/user/user'
					})
				},1000)
			},
			
		}
	}
</script>

<style lang="scss">
	.slot-box {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		align-items: center;
	}

	.slot-image {
		/* #ifndef APP-NVUE */
		display: block;
		/* #endif */
		margin-right: 10px;
		width: 30px;
		height: 30px;
	}

	.slot-text {
		flex: 1;
		font-size: 16px;
		color: #000000;
		margin-right: 10px;
	}

	.progress {
		margin-top: 20upx;
		margin-bottom: 20upx;
	}
	
	.button {
		margin: 10px 80px 0 80px;
		// margin-left: 10px;
		// margin-right: 10px;
	}
	
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
	
	.avatar-text {
		text-align: center;
		font-size: 18px;
		margin-bottom: 5px;
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