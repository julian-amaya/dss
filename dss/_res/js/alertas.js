(function(){
	var interval,
		Alerta = new Class({
			Binds: ['render', 'fetch'],
			sensores: null,
			alerta: null,
			pages: null,
			request: null,
			fecha: null,

			initialize: function(){
				this.sensores = $('sensores')
				this.alerta = $('alerta')
				this.pages = $('pages')
				this.fecha = $('fecha')
				this.request = new Request.JSON({
					url: '/alertas/',
					onSuccess: this.render
				})
				interval = setInterval(this.fetch, 1000)
			},

			render: function(reponse){
				var docfrag = document.createDocumentFragment,
					docfrag2 = document.createDocumentFragment,
					sensores, sensor, alerta, i, fecha,
					cache = {}

				//Alerta
				this.alertas.erase()
				for(i=0;i<reponse.alertas.length; i++){
					alerta = new Element('li', {
						html: '<span>'+reponse.alertas[i].tipo+'</span> <span>'+reponse.alertas[i].sensor+'</span> <span>'+reponse.alertas[i].fecha+'</span>',
						'class': reponse.alertas[i].tipo
						})
					cache[reponse.alertas[i].sensor] = reponse.alertas[i].tipo
					docfrag.appendChild(alerta)
				}
				this.alertas.grab(docfrag.firstChild)

				//Listado
				sensores = reponse.sensores.split(',')
				fecha = sensores.shift()

				this.fecha.set('html', fecha)

				this.sensores.erase()
				for(i=0;i<sensores.length; i++){
					sensor = new Element('li', {
						html: '<span>'+sensores[i].num_sensor+'</span> <span>'+(cache[i]||'OK')+'</span>',
						'class': cache[i]||'OK'
						})
					docfrag2.appendChild(sensor)
				}

				this.sensores.grab(docfrag.firstChild)
				//Paginas
			},

			fetch: function(){
				this.request.get({
					page: this.page
				})
			},

			pageChange: function(){

			}
		}),
		alerta = new Alerta()








})()