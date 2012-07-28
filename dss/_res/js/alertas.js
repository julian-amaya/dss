(function(){
	var interval,
		Alerta = new Class({
			Binds: ['render', 'fetch', 'removeRevised'],
			sensores: null,
			alertas: null,
			alerta: null,
			pages: null,
			request: null,
			fecha: null,
			remove: null,

			/**
			 * Inicializa la clase de Alerta
			 * @return void
			 */
			initialize: function(){
				//Referencas al DOM
				this.sensores = $('sensores')
				this.alerta = $('alerta')
				this.alertas = $('alertas')
				this.pages = $('pages')
				this.fecha = $('fecha')

				//Request objects
				this.request = new Request.JSON({
					url: '/data/',
					onSuccess: this.render
				})
				this.remove = new Request.JSON({
					url: '/mark_alert/',
					onSuccess: function(){}
				})

				//Event listening
				this.alertas.addEvent('click:relay(.revised)', this.removeRevised)

				//Check each second
				// interval = setInterval(this.fetch, 1000)
				this.fetch()
			},

			/**
			 * Renderiza la respuesta del servidor
			 * @param  {Object} response {alertas: [], sensores: 'date,1,2,3,4...'}
			 * @return void
			 */
			render: function(response){
				var docfrag = document.createDocumentFragment(),
					docfrag2 = document.createDocumentFragment(),
					sensores, sensor, alerta, i, fecha,
					cache = {}, zones = {1:0,2:0,3:0,4:0}, zonelimit

				//Load the sensores data or an empty array
				sensores = response.sensores ? response.sensores.split(',') : []
				//How many sensors per each zone
				zonelimit = sensores.length/4
				
				//Carga de Alertas
				this.alertas.empty()
				for(i=0;i<response.alertas.length; i++){
					alerta = new Element('li', {
						html: '<span>'+response.alertas[i].tipo+'</span> <span>'+response.alertas[i].num_sensor+'</span> <span>'+response.alertas[i].fecha_hora+'</span> <button data-id="'+response.alertas[i].num_sensor+'" class="revised">Revisado</button>',
						'class': 't'+response.alertas[i].tipo
						})
					cache[response.alertas[i].sensor] = response.alertas[i].tipo
					if(response.alertas[i].tipo > 2){
						zones[Math.floor(response.alertas[i].num_sensor/zonelimit)] = 1
					}
					docfrag.appendChild(alerta)
				}
				this.alertas.appendChild(docfrag)

				//Carga de Sensores y Fecha
				fecha = sensores.shift()
				this.fecha.set('html', fecha)

				this.sensores.empty()

				console.log(sensores)

				for(i=0;i<sensores.length; i++){
					sensor = new Element('li', {
						html: '<span>'+sensores[i]+'</span> <span>'+(cache[i]||'OK')+'</span>',
						'class': cache[i]||'OK'
						})
					docfrag2.appendChild(sensor)
				}

				this.sensores.appendChild(docfrag2)
				
				//Death Star Alert update
				for(i=0;i<=4;i++){
					if(zones[i]){
						$$('#deathStar .row'+i).removeClass('danger')
					}else{
						$$('#deathStar .row'+i).addClass('danger')
					}
				}
			},

			/**
			 * Carga la info del servidor
			 * @return void
			 */
			fetch: function(){
				this.request.get({
					page: this.page
				})
			},

			/**
			 * Marca una alerta como vista
			 * @param  {Event} evt 
			 * @param  {Element} target elem que lanzó el evento
			 * @return void
			 */
			removeRevised: function(evt, target){
				var id = target.get('data-id')
				target.dispose()
				this.remove.get({id: id})
			}
		}),
		alerta = new Alerta()
})()