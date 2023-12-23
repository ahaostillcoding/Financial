<template>
	<view class="content">
		
			<view class="datetime-picker">
				<uni-datetime-picker ref="showdate" class="datetime" :value="single" type="date" @change="changeLog">
					<uni-row class="test-uni-col">
						<uni-col :span="24" class="test-uni-col">
							<uni-card :is-shadow="true">
								<text class="uni-body" @click="showDate">{{year}}年{{month}}月{{day}}日 {{weekday}}</text>
							</uni-card>
						</uni-col>
					</uni-row>
				</uni-datetime-picker>
			</view>

		
		<uni-row class="demo-uni-row">
			<uni-col :span="12">
				<view class="demo-uni-col light">
					<div class="money-name">总收入</div>
					<div class="money">{{InputSum}}元</div>
				</view>
			</uni-col>
			<uni-col :span="12">
				<view class="demo-uni-col dark">
					<div class="money-name">总支出</div>
					<div class="money">{{OutputSum}}元</div>
				</view>
			</uni-col>
		</uni-row>
		
		<!-- <uni-collapse>
			<uni-collapse-item title="收入" :open="true"> -->
				<uni-group v-if="inputData.length > 0" :title="month + '月' + day + '日'+ '  ' + weekday + '  '+ '   收入'" mode="card">
					<uni-list>
					  <uni-list-chat 
							v-for="item in inputData" 
							key="1"
							v-if="inputData.length > 0"
							class="list-chat" 
							:avatar-circle="true" 
							:title="item.tag" 
							:clickable="true" @click="InputClick(item)"  
							:avatar="item.tagUrl" 
							:note="item.remark"
						>
						<view class="chat-custom-right">
						  <text class="chat-custom-text">+{{ item.money }}元</text>
						  <text class="chat-text">收入</text>
						</view>
					  </uni-list-chat>
					</uni-list>
				</uni-group>
			<!-- </uni-collapse-item>
		</uni-collapse> -->
		
		<!-- <uni-collapse>
			<uni-collapse-item title="支出" :open="true"> -->
				<uni-group v-if="inputData.length > 0" :title="month + '月' + day + '日'+ '  ' + weekday + '  '+ '   支出'" mode="card">
					<uni-list>
					   <uni-list-chat 
					       v-if="inputData.length > 0"
						   v-for="item in outputData" 
						   class="list-chat" 
						   :avatar-circle="true" 
						   :title="item.tag" 
						   :clickable="true" @click="OuputClick(item)" 
						   :avatar="item.tagUrl" 
						   :note="item.remark">			    
							<view class="chat-custom-right"
						>
						  <text class="chat-custom-text">-{{ item.money }}元</text>
						  <text class="chat-text">支出</text>
						</view>
					  </uni-list-chat>
					</uni-list>
				</uni-group>
		<!-- 	</uni-collapse-item>
		</uni-collapse> -->
		
		
	</view>
</template>

<script>
export default {
	data() {
		return {
			showflag: true,
			iconUrl: '', //标签图标
			tag: '',
			InputSum: '', //收入总额
			OutputSum: '', //支出总额
			single: '', //日期选择
			weekday: '',
			year: '',
			month: '',
			day: '',
			inputData: [''], //收入数组
			outputData: [''], //支出数据
			filtered: '', //日期过滤器
		};
	},
	// 下拉刷新	
	onLoad: function (options) {
			setTimeout(function () {
				console.log('start pulldown');
			}, 500);
			uni.startPullDownRefresh();
		},
		onPullDownRefresh() {
			console.log('refresh');
			setTimeout(function () {
				uni.stopPullDownRefresh();
				uni.reLaunch({
					url: 'detail'
				});
			}, 500);
		},
		 
	onLoad() {
		this.getStatus();
		this.getDate() //获取日期
		this.getInput();
		this.getOutput();
		},
	methods: {
	  
	  getStatus() {
		  console.log("status",getApp().globalData.loginstatus)
		  if(getApp().globalData.loginstatus == false){
			  uni.reLaunch({
			  	url: '/pages/login/login'
			  })
		  }else {
			  uni.showLoading({
			  	// title: '加载中'
			  });
			  
			  setTimeout(function () {
			  	uni.hideLoading();
			  }, 500);
		  }
	  },
		// 收入列表点击
	  InputClick(data) {
		let result = {
			id: data._id,
			money: data.money,
			tag: data.tag,
			tagUrl: data.tagUrl,
			datetime: data.datetime,
			remark: data.remark
		}
		var data = JSON.stringify(result);
		// console.log("点击行数据",data)
		uni.redirectTo({
			url: '../../tabbar-3-detial/input/modify?data='+ data
		});
	  },
	  
	  // 支出列表点击
	  OuputClick(data) {
		  let result = {
			id: data._id,
			money: data.money,
			tag: data.tag,
			tagUrl: data.tagUrl,
			datetime: data.datetime,
			remark: data.remark
		  }
		  var data = JSON.stringify(result);
		  // console.log("点击行数据",data)
		uni.redirectTo({
			url: '../../tabbar-3-detial/output/modify?data='+ data
		});
	  },
	  
	  //数据库获取收入金额
	  getInput() {
		  console.log("id",getApp().globalData.loginid)
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
				// console.log('number',number)
				for (let i = 0; i < number; i++) {
					data = result.data[i];
					money = parseFloat(data.money); // 将字符串转换为数值
					InputSum += money;
				}
				this.InputSum = InputSum.toFixed(2); // 将总收入金额赋给 this.InputSum
				// console.log(InputSum)
				
				let data = result.data;  //获取返回数据的data数组
				//根据日期筛选一次
				let filteredData = data.filter(item => item.datetime.startsWith(this.filtered));
				
				// 根据时间排序筛选后的数据
				  filteredData.sort((a, b) => {
					// 将datetime字符串转换为日期对象进行比较
					const dateA = new Date(a.datetime);
					const dateB = new Date(b.datetime);
					return dateB - dateA;
				  });

				this.inputData = filteredData; // 将筛选后的数据赋值给inputData数组
				
		  	},
		  	fail(err) {
		  		console.log('请求失败',err);
		  	}
		  });
	  },
	  
	  //数据库获取支出金额
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
				// console.log('number',number)
				for (let i = 0; i < number; i++) {
					data = result.data[i];
					money = parseFloat(data.money); // 将字符串转换为数值
					OutputSum += money;
				}
				this.OutputSum = OutputSum.toFixed(2); // 将总收入金额赋给 this.OutputSum
				// console.log(OutputSum)
				
				let data = result.data;  //获取返回数据的data数组
				//根据日期筛选当天数据
				let filteredData = data.filter(item => item.datetime.startsWith(this.filtered));
				
				// 根据时间排序筛选后的数据
				filteredData.sort((a, b) => {
				// 将datetime字符串转换为日期对象进行比较	
					const dateA = new Date(a.datetime);
					const dateB = new Date(b.datetime);
					return dateB - dateA;
				});
				
				this.outputData = filteredData; // 将筛选后的数据赋值给inputData数组
		  				
		  	},
		  	fail(err) {
		  		console.log('请求失败',err);
		  	}
		  });
	  },
	 // 获取当前日期
	  getDate() {
		  
		  let currentDate = new Date();
		  let year = currentDate.getFullYear();
		  let month = currentDate.getMonth() + 1;
		  let day = currentDate.getDate();
		  let weekDays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
		   
		  // 返回日期
		  let weekDay = currentDate.getDay();
		  this.month = month;
		  this.day = day;
		  this.year = year;
		  this.weekday = weekDays[weekDay];
		  
		  let filtered = year + '-' + month + '-' + day;
		  this.single = filtered;
		  this.filtered = filtered;
		  console.log('当前显示数据时间',filtered);
 
	  },
	  
	  // 确定日期时间时触发的事件
	  changeLog(e) {
			console.log('改变显示时间:', e);
			this.filtered = e;
			const date = new Date(e);
			const year = date.getFullYear();
			const month = date.getMonth() + 1;
			const day = date.getDate();
			const weekDays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
			const weekDay = date.getDay();
			this.month = month;
			this.day = day;
			this.year = year;
			this.weekday = weekDays[weekDay];
			this.getInput();
			this.getOutput();			
		},
	  showDate() {
		  this.$refs.showdate.show();
		  this.showflag = true;
	  }
	}
};
</script>

<style>
	/* 标签栏 */
	.mb-10 {
		text-align: left;
		}
	.content {
		text-align: center;
		height: 400upx;
		margin-top: 10upx;
	}
	text {
		white-space: pre-wrap;
		text-align: center;
	}
	.money-name {
		padding-top: 10upx;
		padding-left: 20upx;
		text-align: left;
		opacity: 0.6;
	}
	.money {
		padding-top: 6px;
		text-align: center;
		font-size: 45upx;
		font-weight: bold;
	}
	.datetime {
		width: 600upx;
		/* padding: ; */
		/* margin-left: 50upx; */
		margin-left: auto;
		margin-right: auto;
	}
	.time {
		width: 200upx;
		padding-right: 20upx;
		margin-top: 30upx;
		margin-right: 20upx;
	}
	.demo-uni-row {
		margin: 10upx ;
		display: flex;
		justify-content: center;
		/* margin-bottom: 10px; */
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
		height: 120upx;
		/* width: 300upx; */
		border-radius: 5px;
		margin: 0upx 15upx 20upx 20upx;
		border: 3px solid grey;
	}
	
	.test-uni-col {
		border-radius: 5px;
		/* padding-right: 10px; */
		margin-left: auto;
		margin-right: auto;
		
	}
	.datetime-picker {
		display: flex;
		justify-content: center;
	}
	.uni-row {
		border-radius: 5px;
		margin-left: 15upx;
	}
	.dark {
		background-color: #ffffff;
	}
	
	.light {
		background-color: #ffffff;
	}
	.uni-wrap {
		flex-direction: column;
		/* #ifdef H5 */
		height: calc(100vh - 44px);
		/* #endif */
		/* #ifndef H5 */
		height: 100vh;
		/* #endif */
		flex: 1;
	}
	
	.scroll {
		flex-direction: column;
		flex: 1;
	}
	
	.example-body {
		padding: 0;
		/* #ifndef APP-NVUE */
		display: block;
		/* #endif */
	}
	.list-chat {
		text-align: left;
		/* padding-left: 30upx; */
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
	.chat-text {
		font-size: 12px;
		color: #5b5b5b;
		opacity: 0.5;
	}
</style>
