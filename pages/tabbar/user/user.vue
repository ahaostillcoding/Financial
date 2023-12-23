<template>
	<view class="content" >
		
		<view class="login" @click.capture="ToLogin">
			<image :src="avatar"></image>
			<div class="logintext">{{logintext}}</div>
		</view>
		
	
		<view>
			<uni-list class="list">
				<uni-list-item class="list-item" :show-extra-icon="true" showArrow :extra-icon="{color: '',size: '22',type: 'loop'}" title="检查更新" clickable  @click="onClick" ></uni-list-item>
				<uni-list-item class="list-item" :show-extra-icon="true" showArrow :extra-icon="{color: '',size: '22',type: 'gear'}" title="设置" clickable @click="setting"></uni-list-item>
				<uni-list-item class="list-item" :show-extra-icon="true" showArrow :extra-icon="{color: '',size: '22',type: 'gear'}" title="使用帮助" clickable @click="help"></uni-list-item>
			</uni-list>
		</view>
		
	</view>
	
	
</template>

<script>
	export default {
		data() {
			return {
				logintext: '登录',
				avatar: 'https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora%E5%9B%BE%E7%89%87/me.png',  //头像
				zhiwen_flag: -1,
				id: ''
			}
		},
		onLoad: function (option) {
			if(option.data != null){
				var result = JSON.parse(option.data)
				console.log("接受数据",result)
				this.logintext = result[0].name
				this.avatar = result[0].avatar
				// this.id = result[0]._id
				console.log("id",result[0]._id)
				// console.log("用户名称",result[0].name)
			}else {
				console.log("数据为空")
			}	
		},
		onLoad() {
			this.getStatus()
		 
		},
		methods: {
			getStatus() {
				if(getApp().globalData.loginstatus == false){
				    uni.reLaunch({
					  url: '/pages/login/login'
					})
				}else{
					this.getUser()
				}
			},
			getUser() {
				this.logintext = getApp().globalData.loginname,
				this.avatar = getApp().globalData.loginavatar
			},
			onClick(e) 
			{
				console.log('执行click事件', e.data)
				uni.showToast({
					title: '已经是最新版本'
				});
			},			
			ToLogin() {
				if(this.logintext != '登录'){
					const data = {
					  userAvatar: this.avatar,
					  name: this.logintext,
					  id: this.id
					};
					// 将数据对象转换为 JSON 字符串
					const jsonData = JSON.stringify(data);
					uni.navigateTo({
					  url: '/pages/tabbar/user/admin?data=' + encodeURIComponent(jsonData),
					});
				}
				else {
					uni.navigateTo({
						url: '/pages/login/login',
						events: {
						    // 为指定事件添加一个监听器，获取被打开页面传送到当前页面的数据
						    acceptDataFromOpenedPage: function(data) {
						      console.log(data)
						    },
						    someEvent: function(data) {
						      console.log(data)
						    }
						  },
						  success: function(res) {
						    // 通过eventChannel向被打开页面传送数据
						    res.eventChannel.emit('acceptDataFromOpenerPage', { data: 'data from starter page' })
						  }
					});
				}
				
			},
			setting() {
				uni.navigateTo({
					url: 'setting'
				})
			},
			help() {
				// location.href ='https://cn.bing.com/';
				uni.navigateTo({
					url: '/pages/tabbar/user/help'
				})
			}
		}
	}
</script>

<style>
	.content {
		text-align: center;
		margin-top: 50upx;
	}
	.list{
		text-align: left;
		margin-top: 180upx;
		margin-left: 20upx;
		margin-right: 20upx;
	}
	.list-item {
		margin-top: 10upx;
	}
	.center {
		flex: 1;
		flex-direction: column;
		background-color: #f8f8f8;
	}
	image {
		width: 180rpx;
		height: 180rpx;
	}
	.login {
		text-align: center;
		height: 100upx;
		margi: 50upx;
	}
	.logintext {
		font-size: 20px;
	}
</style>
