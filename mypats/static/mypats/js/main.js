// 调用HTML5 GeoLocation API获取地理位置
    function getLocation(){

        document.getElementById('container').innerHTML = '正在搜寻中，请稍候。。。';

        var options = {
            enableHighAccuracy:true, 
            maximumAge:1000
        }

        if(navigator.geolocation){
            //浏览器支持geolocation
            navigator.geolocation.getCurrentPosition(onSuccess,onError,options);
			
        }else{
            //浏览器不支持geolocation
            alert('浏览器不支持GeoLocation!');
        }
    }

    // 获取成功
    function onSuccess(position){

		
        // 经度
        var longitude =position.coords.longitude;

        // 纬度
        var latitude = position.coords.latitude;

		//根据坐标逆解析地址  

		//alert("坐标经度为：" + latitude + "， 纬度为：" + longitude );  
        gpsPoint = new BMap.Point(longitude, latitude);    // 创建点坐标  

		var geoc = new BMap.Geocoder();  
		var address = geoc.getLocation(gpsPoint, getCityByCoordinate);  		
		

        // 使用百度地图API创建地图实例  
        var map =new BMap.Map("container");

        // 创建一个坐标
        var point =new BMap.Point(longitude,latitude);

        // 地图初始化，设置中心点坐标和地图级别  
        map.centerAndZoom(point, 16);

        // 设置标注的图标,可自己定义图标
        var icon = new BMap.Icon("http://api.map.baidu.com/img/markers.png", new BMap.Size(23, 25), {  
            offset: new BMap.Size(10, 25),              // 定位图标尺寸  
            imageOffset: new BMap.Size(0, 0 - 11 * 25)  // 设置图片偏移  
        }); 

        // 设置标注的经纬度
        var marker = new BMap.Marker(new BMap.Point(longitude,latitude),{icon:icon});

        // 把标注添加到地图上
        map.addOverlay(marker);

		map.enableScrollWheelZoom();  // 开启鼠标滚轮缩放    
		map.enableKeyboard();         // 开启键盘控制    
		map.enableContinuousZoom();   // 开启连续缩放效果    
		map.enableInertialDragging(); // 开启惯性拖拽效果  

		map.addControl(new BMap.NavigationControl()); //添加标准地图控件(左上角的放大缩小左右拖拽控件)  
		map.addControl(new BMap.ScaleControl());      //添加比例尺控件(左下角显示的比例尺控件)  
		map.addControl(new BMap.OverviewMapControl()); // 缩略图控件  
		map.addControl(new BMap.MapTypeControl());


        // 设置点击事件
        //marker.addEventListener("click", function(){
        //   alert("经度:" + longitude + ", 纬度:" + latitude);
        //});

		var data_info = [[116.417854,39.921988,"<div id='content' class='row'><div class='col-sm-5 img_logo'><img src='img/spokeman.png' class='img-responsive'/></div><div class='col-sm-7'><p>英雄</p><p>BJ1345</p><div class='star-rating' id='star0'></div>", 3],
				 [116.406605,39.921585,"<div id='content' class='row'><div class='col-sm-5 img_logo'><img src='img/spokeman.png' class='img-responsive'/></div><div class='col-sm-7'><p>英雄</p><p>BJ1345</p><div class='star-rating' id='star1'></div>", 4],
				 [116.412222,39.912345,"<div id='content' class='row'><div class='col-sm-5 img_logo'><img src='img/spokeman.png' class='img-responsive'/></div><div class='col-sm-7'><p>英雄</p><p>BJ1345</p><div class='star-rating' id='star2'></div>", 5]
				];
		var opts = {
					width : 250,     // 信息窗口宽度
					height: 110,     // 信息窗口高度
					title : "" , // 信息窗口标题
					enableMessage:true//设置允许信息窗发送短息
				   };
		for(var i=0;i<data_info.length;i++){
			var marker = new BMap.Marker(new BMap.Point(data_info[i][0],data_info[i][1]));  // 创建标注
			var content = data_info[i][2];

			var star_content = "<div>";

			// display rating html
			for (var j = 0; j < data_info[i][3]; j ++)
			{
				star_content += "<img src='img/star-on.png' />";
			}
			for (var j = data_info[i][3]; j < 5; j ++)
			{
				star_content += "<img src='img/star-off.png' />";
			}
			content += star_content;
			content += "</div></div>"

			map.addOverlay(marker);               // 将标注添加到地图中
			addClickHandler(content,marker);

			//openInfo(content, marker)
			
		}

		function addClickHandler(content,marker){
			marker.addEventListener("click",function(e){
				openInfo(content,e)}
			);
		}
		function openInfo(content,e){
			var p = e.target;
			//var p = e;
			var point = new BMap.Point(p.getPosition().lng, p.getPosition().lat);
			var infoWindow = new BMap.InfoWindow(content,opts);  // 创建信息窗口对象 
			map.openInfoWindow(infoWindow,point); //开启信息窗口
			//infoWindow.redraw();

			//var star_id = "#star" + i;
			//star_id = "#star0";
			//star_id = #

			//$(star_id).raty({number : 5});
			//$(star_id).raty({score : 3});

			
		}

    }

    // 获取失败
    function onError(error){
        switch(error.code){
            case 1:
                alert("位置服务被拒绝");
            break;

            case 2:
                alert("暂时获取不到位置信息");
            break;

            case 3:
                alert("获取信息超时");
            break;

            case 4:
                alert("未知错误");
            break;
        }
    }

	 function getCityByCoordinate(rs) {  
		gpsAddress = rs.addressComponents;  
		var address = "GPS标注：" + gpsAddress.province + "," + gpsAddress.city + "," + gpsAddress.district + "," + gpsAddress.street + "," + gpsAddress.streetNumber;  
		
		$('#address').text(address);
	}  

    window.onload = getLocation;