'use strict';
const db = uniCloud.database()
exports.main = async (event, context) => {
	//event为客户端上传的参数
	console.log('用户ID : ', event.userID)
	let collection = db.collection("output")
	//获取数据库的信息
	let res = await collection.where({userID: event.userID}).get()
	// let data = res.data
	// // let money = data[0].money
	// // console.log("money",money)
	// // console.log("data",data)
	// console.log("res",res)
	//返回数据给客户端
	return res
};
