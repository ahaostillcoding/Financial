<template>
	<view>
		<uni-list class="list">
			<uni-list-item :show-extra-icon="true" clickable  @click="admin" showArrow :extra-icon="{color: '',size: '22',type: 'person'}" title="账号设置" ></uni-list-item>
			<uni-list-item :show-extra-icon="true" showArrow :extra-icon="{color: '',size: '22',type: 'circle-filled'}" :variable="zhiwen_flag" title="指纹登录"  :show-switch="true"  @switchChange="zhiwen" ></uni-list-item>
		</uni-list>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				zhiwen_flag: '',
			}
		},
		methods: {
			zhiwen() {
				console.log("指纹登陆")
			},
			admin() {
				uni.navigateTo({
				  url: '/pages/tabbar/user/admin',
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
				})
			},
		}
	}
</script>

<style>

</style>
