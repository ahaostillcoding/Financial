<template>
	<view class="content">

		<view class="select">
			<uni-data-select class="select-text" v-model="value" :localdata="range" :clear="false"
				@change="change"></uni-data-select>
		</view>

		<uni-row class="demo-uni-row">
			<uni-col :span="8">
				<view class="demo-uni-col dark" @click="chooseWeek" :style="{ backgroundColor: weekColor }">
					<text class="text">周</text>
				</view>
			</uni-col>
			<uni-col :span="8">
				<view class="demo-uni-col light" @click="chooseMonth" :style="{ backgroundColor: monthColor }">
					<text class="text">月</text>
				</view>
			</uni-col>
			<uni-col :span="8">
				<view class="demo-uni-col dark_deep" @click="chooseYear" :style="{ backgroundColor: yearColor }">
					<text class="text">年</text>
				</view>
			</uni-col>
		</uni-row>

		<view v-if="showOutput">

			<uni-row class="demo-uni-row">
				<uni-col :span="12">
					<view class="test-uni-col light">
						<div class="money-name">总支出</div>
						<div class="money">{{OutputSum}}元</div>
					</view>
				</uni-col>
				<uni-col :span="12">
					<view class="test-uni-col dark">
						<div class="money-name">平均支出</div>
						<div class="money">{{AverageOutput}}元</div>
					</view>
				</uni-col>
			</uni-row>

			<uni-group v-if="outputData && outputData.length > 0" :title="cardtitile + '  支出排行榜'" mode="card">
				<uni-list>
					<uni-list-chat v-for="item in outputData" :key="item.tag" class="list-chat" :avatar-circle="true"
						:title="item.tag" :clickable="true" @click="OuputClick(item)" :avatar="item.tagUrl">
						<view class="chat-custom-right">
							<text class="chat-custom-text">-{{ item.money }}元</text>
							<text class="chat-text">支出</text>
						</view>
					</uni-list-chat>
				</uni-list>
			</uni-group>

		</view>


		<!-- 		<view class="progress-box">
			<progress :percent="80" stroke-width="3" />
		</view> -->

		<view v-if="showInput">

			<uni-row class="demo-uni-row">
				<uni-col :span="12">
					<view class="test-uni-col light">
						<div class="money-name">总收入</div>
						<div class="money">{{InputSum}}元</div>
					</view>
				</uni-col>
				<uni-col :span="12">
					<view class="test-uni-col dark">
						<div class="money-name">平均收入</div>
						<div class="money">{{AverageInput}}元</div>
					</view>
				</uni-col>
			</uni-row>

			<uni-group v-if="inputData && inputData.length > 0" :title="cardtitile + ' 收入排行榜'" mode="card">
				<uni-list>
					<uni-list-chat v-for="item in inputData" class="list-chat" :avatar-circle="true" :title="item.tag"
						:clickable="true" @click="OuputClick(item)" :avatar="item.tagUrl">
						<view class="chat-custom-right">
							<text class="chat-custom-text">+{{ item.money }}元</text>
							<text class="chat-text">收入</text>
						</view>
					</uni-list-chat>
				</uni-list>
			</uni-group>

		</view>




	</view>
</template>
<script>
	export default {
		data() {
			return {
				item: null,
				showInput: false,
				showOutput: true,
				iconUrl: '', //标签图标
				tag: '',
				InputSum: '', //收入总额
				OutputSum: '', //支出总额
				AverageOutput: '', //平均支出
				AverageInput: '', //平均收入
				weekday: '',
				year: '',
				month: '',
				day: '',
				inputData: [], //收入数组
				outputData: [], //支出数据
				option: 'week',
				//获取当前周
				startDate: '',
				endDate: '',
				cardtitile: '',
				// startMonth: '',

				weekColor: '#55aaff',
				monthColor: '#ffffff',
				yearColor: '#ffffff',

				value: 0,
				range: [{
						value: 0,
						text: "支出"
					},
					{
						value: 1,
						text: "收入"
					},
				],
			};
		},

		onLoad() {
			this.getStatus()
			this.getDate(this.option)
			this.getOutput()
			this.getInput()
		},

		methods: {
			getStatus() {
				console.log("status", getApp().globalData.loginstatus)
				if (getApp().globalData.loginstatus == false) {
					uni.reLaunch({
						url: '/pages/login/login'
					})
				} else {
					uni.showLoading({
						// title: '加载中'
					});

					setTimeout(function() {
						uni.hideLoading();
					}, 500);
				}
			},
			// 显示支出还是收入
			change(e) {
				console.log("e:", e);
				// e=1 为收入
				if (e == 1) {
					this.showInput = true;
					this.showOutput = false;
				} else {
					this.showInput = false;
					this.showOutput = true;
				}
			},
			OuputClick(data) {
				// console.log('outputData数组',this.outputData)
				uni.showToast({
					title: '点击'
				})
				setTimeout(function() {
					uni.reLaunch({
						url: '../detail/detail'
					})
				}, 500);

			},
			chooseWeek() {
				console.log('周点击');
				this.option = 'week';
				this.getDate(this.option)
				this.getOutput()
				this.getInput()
				this.$set(this.outputData)
				this.$set(this.inputData)
				this.weekColor = '#55aaff';
				this.monthColor = '#ffffff';
				this.yearColor = '#ffffff';
			},
			chooseMonth() {
				this.option = 'month';
				console.log('月点击');
				this.getDate(this.option)
				this.getOutput()
				this.getInput()
				this.$set(this.outputData)
				this.$set(this.inputData)
				// this.$forceUpdate();
				this.weekColor = '#ffffff';
				this.monthColor = '#55aaff';
				this.yearColor = '#ffffff';
			},
			chooseYear() {
				this.option = 'year';
				console.log('年点击');
				this.getDate(this.option)
				this.getOutput()
				this.getInput()
				this.$set(this.outputData)
				this.$set(this.inputData)
				this.weekColor = '#ffffff';
				this.monthColor = '#ffffff';
				this.yearColor = '#55aaff';
			},

			getOutput() {
				uniCloud.callFunction({
					name: 'getOutput',
					data: {
						userID: getApp().globalData.loginid,
					},
					success: res => {
						let result = res.result
						let money = 0;
						let OutputSum = 0;
						let number = result.affectedDocs
						// console.log("startDate",this.startDate)
						// result.data.forEach(item => {
						// 	OutputSum += parseFloat(item.money)
						// })
						// this.OutputSum = OutputSum.toFixed(2); // 总支出金额
						// this.AverageOutput = (OutputSum / number).toFixed(2) //平均收入

						// if(option == 'week')
						// {
						result.data.forEach(item => {
							let itemDate = new Date(item.datetime); // 将数据库中的datetime时间转换为Date对象
							if (itemDate >= this.startDate && itemDate <= this
								.endDate) { // 与当前一周的时间范围进行比较
								OutputSum += parseFloat(item.money);
							}
						});
						this.OutputSum = OutputSum.toFixed(2);
						this.AverageOutput = (OutputSum / number).toFixed(2);

						let data = result.data;
						let categoryTotals = {};
						data.forEach(item => {
							let itemDate = new Date(item.datetime);
							// 显示当前周的数据
							if (itemDate >= this.startDate && itemDate <= this.endDate) {
								let category = item.tag;
								let amount = parseFloat(item.money);
								if (categoryTotals.hasOwnProperty(category)) {
									categoryTotals[category].money += amount;
								} else {
									categoryTotals[category] = {
										tag: item.tag,
										tagUrl: item.tagUrl,
										money: amount
									};
								}
							}
						});

						let outputData = Object.values(categoryTotals).map(category => ({
							tag: category.tag,
							tagUrl: category.tagUrl,
							money: category.money
						}));

						outputData.sort((a, b) => b.money - a.money); // 根据金额从大到小排序

						this.outputData = outputData;

						// console.log("outputdata",JSON.stringify(outputData))

					},
					fail(err) {
						console.log('请求失败', err);
					}
				});
			},

			getInput() {
				uniCloud.callFunction({
					name: 'getInput',
					data: {
						userID: getApp().globalData.loginid,
					},
					success: res => {
						let result = res.result
						let money = 0;
						let InputSum = 0;
						let number = result.affectedDocs
						result.data.forEach(item => {
							let itemDate = new Date(item.datetime); // 将数据库中的datetime时间转换为Date对象
							if (itemDate >= this.startDate && itemDate <= this
								.endDate) { // 与当前一周的时间范围进行比较
								InputSum += parseFloat(item.money);
							}
						});
						this.InputSum = InputSum.toFixed(2);
						this.AverageInput = (InputSum / number).toFixed(2);

						let data = result.data;
						let categoryTotals = {};
						data.forEach(item => {
							let itemDate = new Date(item.datetime);
							// 显示当前周的数据
							if (itemDate >= this.startDate && itemDate <= this.endDate) {
								let category = item.tag;
								let amount = parseFloat(item.money);
								if (categoryTotals.hasOwnProperty(category)) {
									categoryTotals[category].money += amount;
								} else {
									categoryTotals[category] = {
										tag: item.tag,
										tagUrl: item.tagUrl,
										money: amount
									};
								}
							}
						});

						let inputData = Object.values(categoryTotals).map(category => ({
							tag: category.tag,
							tagUrl: category.tagUrl,
							money: category.money
						}));

						inputData.sort((a, b) => b.money - a.money); // 根据金额从大到小排序

						this.inputData = inputData;

						// console.log("inputdata",JSON.stringify(inputData))

					},
					fail(err) {
						console.log('请求失败', err);
					}
				});
			},


			// 获取当前日期
			getDate(option) {
				let currentDate = new Date();
				let year = currentDate.getFullYear();
				let month = currentDate.getMonth() + 1;
				let day = currentDate.getDate();
				let weekDays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];

				let weekDay = currentDate.getDay();
				this.month = month;
				this.day = day;
				this.year = year;
				this.weekday = weekDays[weekDay];

				let startDate, endDate;

				if (option === 'week') {
					startDate = new Date(currentDate);
					startDate.setDate(day - weekDay + 1); // 当前日期减去星期几的天数，得到本周的周一
					endDate = new Date(startDate);
					endDate.setDate(startDate.getDate() + 6); // 本周的周一加6天，得到本周的周日
				} else if (option === 'month') {
					startDate = new Date(year, month - 1, 1); // 当前月份的第一天
					endDate = new Date(year, month, 0); // 当前月份的最后一天
				} else if (option === 'year') {
					startDate = new Date(year, 0, 1); // 当前年份的第一天
					endDate = new Date(year, 11, 31); // 当前年份的最后一天
				}

				let startYear = startDate.getFullYear();
				let startMonth = startDate.getMonth() + 1;
				let startDay = startDate.getDate();
				let endYear = endDate.getFullYear();
				let endMonth = endDate.getMonth() + 1;
				let endDay = endDate.getDate();

				this.startDate = startDate;
				this.endDate = endDate;

				let filtered = startYear + '-' + startMonth + '-' + startDay + ' 至 ' + endYear + '-' + endMonth + '-' +
					endDay;
				this.cardtitile = filtered
				console.log('当前显示数据时间', filtered);
			}

		},
	};
</script>
<style lang="scss">
	.content {
		text-align: center;
		height: 400upx;
		margin-top: 20upx;
	}

	.demo-uni-row {
		margin-bottom: 20upx;
		margin-left: 15upx;
		margin-right: 15upx;
		/* QQ、抖音小程序文档写有 :host，但实测不生效 */
		/* 百度小程序没有 :host，需要设置block */
		/* #ifdef MP-TOUTIAO || MP-QQ || MP-BAIDU */
		display: block;
		/* #endif */
	}

	/* 支付宝小程序没有 demo-uni-row 层级 */
	/* 微信小程序使用了虚拟化节点，没有 demo-uni-row 层级 */
	/* #ifdef MP-ALIPAY || MP-WEIXIN */
	/deep/ .uni-row {
		margin-bottom: 10px;
	}

	/* #endif */

	.demo-uni-col {
		margin-left: 5upx;
		margin-right: 5upx;
		height: 36px;
		border-radius: 4px;
		border: 1px solid grey;
		font-size: 40upx;
		text-align: center;
		// font-weight: bold;
	}

	.test-uni-col {
		margin-left: 15upx;
		margin-right: 15upx;
		height: 120upx;
		border-radius: 4px;
		border: 3px solid grey;
		font-size: 40upx;
		// font-weight: bold;
	}

	.dark_deep {
		background-color: #ffffff;
	}

	.dark {
		background-color: #ffffff;
	}

	.light {
		background-color: #ffffff;
	}

	.text {
		margin-top: 10upx;
		text-align: center;
	}

	.select {
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 20upx;
		border-radius: 4px;
		width: 250upx;
		background-color: #ffffff;
		// font-size: 50upx;
	}

	.select-text {
		// font-size: 50upx;
	}

	.chat-text {
		font-size: 12px;
		color: #5b5b5b;
		opacity: 0.5;
	}

	.money-name {
		padding-top: 10upx;
		padding-left: 20upx;
		text-align: left;
		opacity: 0.6;
		font-size: 15px;
	}

	.money {
		
		padding-top: 6px;
		text-align: center;
		font-size: 45upx;
		font-weight: bold;
	}

	.chat-custom-right {
		flex: 1;
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: column;
		justify-content: space-between;
		align-items: flex-end;
	}

	.chat-custom-text {
		font-size: 20px;
		color: #4d4d4d;
	}

	.list-chat {
		text-align: left;
	}
</style>