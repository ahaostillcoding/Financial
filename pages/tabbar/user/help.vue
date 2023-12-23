<template>
	<!-- <view>
		<web-view src="https://www.dcloud.io///"></web-view>
	</view> -->
	<button @click="out">导出</button>
</template>

<script>
	export default {
		data() {
			return {
				url: '',
				userData: [],
			}
		},
		// onLoad(item) {
		//     this.url = decodeURIComponent(item.url)
		//     // 传入需要跳转的链接 使用web-view标签进行跳转
		//   },
		onLoad() {
			this.getOutput();
			// let item = 'https://cn.bing.com/'
			//    this.url = decodeURIComponent(item.url)
			//    // 传入需要跳转的链接 使用web-view标签进行跳转
		},
		methods: {
			getOutput() {
				uniCloud.callFunction({
					name: 'getOutput',
					data: {
						userID: '658439c3a7c432e4a3cf8443',
					},
					success: res => {
						// this.userData = JSON.stringify(res.result.data)
						this.userData = res.result.data
						// console.log("用户支出数据",this.userData)
					},
					fail(err) {
						console.log('请求失败', err);
					}
				});
			},
			out() {
				// this.getOutput();
				console.log("用户支出数据", this.userData);
				const json_data = {
					data: this.userData
				};
				console.log('json', json_data)
				// uni.request({
				// 	url: 'http://127.0.0.1:7800/json',
				// 	method: 'POST',
				// 	header: {
				// 		'content-type': 'application/json',
				// 	},
				// 	data: json_data,
				// 	success: (res) => {
				// 		// 解析返回的 JSON 数据
				// 		console.log('导出数据结果', res.data);
				// 		const ossUrl = res.data.url;
				// 		console.log(ossUrl)
				// 	},
				// 	fail: (err) => {
				// 		console.error('导出数据失败', err);
				// 	}
				// })
				// uniCloud.callFunction({
				//   name: 'txt',
				//   data: {
				//     data: this.userData
				//   },
				//   success: res => {
				//     // console.log("导出数据",res.result)
				//     let url = res.result.url;
				//     // console.log("返回url",url)
				//     this.url = url;
				//     console.log("获取url", url);
				//   }
				// });

			},
		}
	}
</script>

<style>

</style>