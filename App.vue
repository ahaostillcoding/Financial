<script>
export default {
	
	//设置全局变量
	globalData: {  
	    loginname: '',
		loginavatar: '',
		loginstatus: 0, //0表示未登录
		loginid: '', //用户id
	}, 
	onLaunch: function() {
		console.log('App Launch');

		// setTimeout(() => {
		// 	uni.setTabBarBadge({
		// 		index: 1,
		// 		text: '31'
		// 	});
		// 	uni.showTabBarRedDot({
		// 		index: 3
		// 	});
		// }, 1000);
	},
	onShow: function() {
		console.log('App Show');
	},
	onHide: function() {
		console.log('App Hide');
	}
};
</script>

<style>
/*每个页面公共css */ 
</style>
