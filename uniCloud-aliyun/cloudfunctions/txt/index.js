'use strict';
exports.main = async (event, context) => {
    const url = "http://127.0.0.1:8800/json"; // 替换为服务器的实际地址
    // console.log("云函数收到数据", event.data)
    // 构造请求的JSON数据
    // 去除请求参数中的转义字符
    const unescapedData = event.data.replace(/\\\"/g, '"');

    // 解析请求参数中的数组
    const dataArray = JSON.parse(unescapedData);

    const json_data = {
      "data": dataArray
    };
    // 发送POST请求
    const response = await uniCloud.httpclient.request(url, {
      method: 'POST',
      contentType: 'json',
      data: json_data
    });
    // 解析返回的 JSON 数据
    // const responseData = JSON.parse(response.data);
    // console.log("导出数据结果", responseData);
    // const ossUrl = responseData.url;
    // // console.log(ossUrl)
    // return {
    //   code: 200,
    //   msg: '导出成功',
    //   url: ossUrl
    // };
	 if (response.statusCode === 200) {
	      // POST请求成功
	      console.log("导出数据成功");
	      const responseData = JSON.parse(response.data);
	      const ossUrl = responseData.url;
	      return {
	        code: 200,
	        msg: '导出成功',
	        url: ossUrl
	      };
	    } else {
	      // POST请求失败
	      console.error("导出数据失败，状态码：", response.statusCode);
	      return {
	        code: response.statusCode,
	        msg: '导出失败'
	      };
	    }
};