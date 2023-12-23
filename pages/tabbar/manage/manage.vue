<template>
	<view class="page container">
		<view class="select">
			<uni-data-select class="select-text" v-model="value" :localdata="ranges" :clear="false"
				@change="change"></uni-data-select>
		</view>

		<view>
			<uni-card class="uni-card">
				<text class="uni-body">请选择导出{{name}}数据日期范围</text>
			</uni-card>
		</view>

		<view class="example-body">
			<uni-datetime-picker v-model="range" type="daterange" @maskClick="maskClick" />
		</view>

		<!-- <button @click="out">导出数据</button> -->
		<!-- 支出 -->
		<view v-if="showTag">
			<button type="primary" class="dataButton" @click="out(0)">导出为Excel</button>
			<button type="primary" class="dataButton" @click="out(1)">导出为txt</button>
			<button type="primary" class="dataButton" @click="open">打开文件</button>
		</view>
		<!-- 收入 -->
		<view v-if="showTag2">
			<button type="primary" class="dataButton" @click="Input(0)">导出为Excel</button>
			<button type="primary" class="dataButton" @click="Input(1)">导出为txt</button>
			<button type="primary" class="dataButton" @click="open">打开文件</button>
		</view>

	</view>
</template>
<script>
	export default {
		data() {
			return {
				showTag: true, 
				showTag2: false,
				url: '', //支出url
				InUrl: '', //收入url
				userData: [],
				userInData: [], //收入数据
				value: 0,
				option: '0',
				ranges: [{
						value: 0,
						text: "支出"
					},
					{
						value: 1,
						text: "收入"
					},
				],
				name: '支出',
				currentMonthDates: [],
				single: '',
				range: ['2023-01-1', '2023-12-31'],
				currentDate: '',
			}
		},

		watch: {
			range(newval) {
				console.log('范围选:', this.range);
			},

		},
		onLoad() {
			this.getStatus();
			this.getOutput()
			this.getIntput()
			this.getCurrentMonthDates();
		},
		methods: {
			getStatus() {
				// console.log("status",getApp().globalData.loginstatus)
				if (getApp().globalData.loginstatus == false) {
					uni.reLaunch({
						url: '/pages/login/login'
					})
				} else {}
			},
			change(e) {
				console.log("e:", e);
				// e=1 为收入
				uni.showLoading({
					// title: '导出数据中'
				})
				setTimeout(function() {
					uni.hideLoading()
				}, 500)
				if (e == 1) {
					this.name = '收入'
					this.option = 1
					this.showTag2 = true
					this.showTag = false
				} else {
					this.name = '支出'
					this.option = 0
					this.showTag2 = false
					this.showTag = true
				}
			},
			getCurrentMonthDates() {
				const currentDate = new Date();
				const currentMonthFirstDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
				const currentMonthLastDay = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);

				const firstDay = this.formatDate(currentMonthFirstDay);
				const lastDay = this.formatDate(currentMonthLastDay);

				this.currentMonthDates = [firstDay, lastDay];
				this.range = [firstDay, lastDay];
				console.log('日期', this.currentMonthDates)

			},
			formatDate(date) {
				const year = date.getFullYear();
				const month = (date.getMonth() + 1).toString().padStart(2, '0');
				const day = date.getDate().toString().padStart(2, '0');
				return `${year}-${month}-${day}`;
			},
			maskClick(e) {
				console.log('maskClick事件:', e);
			},
			getOutput() {
				uniCloud.callFunction({
					name: 'getOutput',
					data: {
						userID: getApp().globalData.loginid,
					},
					success: res => {
						this.userData = JSON.stringify(res.result.data)
						// console.log("用户支出数据",this.userData)
					},
					fail(err) {
						console.log('请求失败', err);
					}
				});
			},
			out(option) {		
				this.getOutput()
				// console.log("用户支出数据",this.userData)
				console.log('导出支出数据')
				
				// const json_data = {
				// 	data: this.userData
				// };
				// console.log('json',json_data)
				// uni.request({
				// 	url: 'http://127.0.0.1:7800/json',
				// 	method: 'POST',
				// 	header: {
				// 		'content-type': 'application/json',
				// 	},
				// 	data: json_data,
				// 	success: (res) => {
				// 		// 解析返回的 JSON 数据
				// 		const responseData = JSON.parse(res.data);
				// 		console.log('导出数据结果', responseData);
				// 		const ossUrl = responseData.url;
				// 		// console.log(ossUrl)
				// 	},
				// 	fail: (err) => {
				// 		console.error('导出数据失败', err);
				// 	}
				// 	})
				//导出为excel
				if(option == 0){
					uni.showLoading({
						title: '导出为Excel'
					})
					setTimeout(function() {
						uni.hideLoading()
					}, 2000)
					uniCloud.callFunction({
						name: 'excel',
						data: {
							data: this.userData
						},
						success: res => {
								// console.log("导出数据",res.result)
								let url = res.result.url
								// console.log("返回url",url)
								this.url = url;
								console.log("获取url",url)
						}
					})
				}else {
					uni.showLoading({
						title: '导出为txt'
					})
					setTimeout(function() {
						uni.hideLoading()
					}, 2000)
					uniCloud.callFunction({
						name: 'txt',
						data: {
							data: this.userData
						},
						success: res => {
								// console.log("导出数据",res.result)
								let url = res.result.url
								// console.log("返回url",url)
								this.url = url;
								console.log("获取url",url)
						}
					})
				}
			},

			getIntput() {
				uniCloud.callFunction({
					name: 'getInput',
					data: {
						userID: getApp().globalData.loginid,
					},
					success: res => {
						this.userInData = JSON.stringify(res.result.data)
						// console.log("用户支出数据",this.userInData)
					},
					fail(err) {
						console.log('请求失败', err);
					}
				});
			},
			Input(option) {
				this.getIntput()
				console.log("导出收入数据")
				if(option == 0){
					uni.showLoading({
						title: '导出为Excel'
					})
					setTimeout(function() {
						uni.hideLoading()
					}, 2000)
					uniCloud.callFunction({
						name: 'excel',
						data: {
							data: this.userInData
						},
						success: res => {
								// console.log("导出数据",res.result)
								let url = res.result.url
								// console.log("返回url",url)
								this.url = url;
								console.log("获取url",url)
						}
					})
				}else {
					uni.showLoading({
						title: '导出为txt'
					})
					setTimeout(function() {
						uni.hideLoading()
					}, 2000)
					uniCloud.callFunction({
						name: 'txt',
						data: {
							data: this.userInData
						},
						success: res => {
								// console.log("导出数据",res.result)
								let url = res.result.url
								// console.log("返回url",url)
								this.url = url;
								console.log("获取url",url)
						}
					})
				}
			},

			open() {
				//支出数据
				if (this.option == 0) {
					uni.downloadFile({
						url: this.url,
						// url: 'https://digitalhuman1.oss-cn-beijing.aliyuncs.com/data_01f6aa5c-1ea2-4185-a9a4-89901d9f4786.xlsx',
						success: function(res) {
							var filePath = res.tempFilePath;
							uni.openDocument({
								filePath: filePath,
								showMenu: true,
								success: function(res) {
									console.log('打开文档成功');
								}
							});
						}
					});
				} else { //收入数据
					uni.downloadFile({
						url: 'this.InUrl',
						success: function(res) {
							var filePath = res.tempFilePath;
							uni.openDocument({
								filePath: filePath,
								showMenu: true,
								success: function(res) {
									console.log('打开文档成功');
								}
							});
						}
					});
				}

			}
		}
	}
</script>
<style lang="scss">
	.example-body {
		background-color: #fff;
		padding: 20px;
	}

	.uni-body {
		text-align: center;
		font-size: 18px;
	}

	.select {
		margin-top: 10px;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 20upx;
		border-radius: 4px;
		width: 250upx;
		background-color: #ffffff;
		// font-size: 50upx;
	}

	.uni-card {
		text-align: center;
	}

	.select-text {
		// font-size: 50upx;
		text-align: center;
	}

	.dataButton {
		margin-top: 20px;
		margin-left: 100px;
		margin-right: 100px;
	}
</style>