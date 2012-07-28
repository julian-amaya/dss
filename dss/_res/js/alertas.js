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
			zonelimit: 0,
			alertas_cache: [],

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

				//Event listening
				this.alertas.addEvent('click:relay(.revised)', this.removeRevised)
				this.sensores.addEvent('click:relay(.sensor)', this.showChart)

				//Check each second
				interval = setInterval(this.fetch, 1000)
				google.load("visualization", "1", {packages:["corechart"]});
				google.setOnLoadCallback(function(){
					var data = google.visualization.arrayToDataTable([
							['Year', 'Sales', 'Expenses'],
							['2004',  1000,      400],
							['2005',  1170,      460],
							['2006',  660,       1120],
							['2007',  1030,      540]
						]);

						var options = {
						title: 'Company Performance'
						};

						var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
							chart.draw(data, options);
						}
				})
				// this.fetch()
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
					cache = {},
					errorNames = {3: 'Ataque', 4: 'Defectuoso'}


				//Load the sensores data or an empty array
				sensores = response.sensores ? response.sensores.split(',') : []
				//How many sensors per each zone
				
				//Carga de Alertas
				if(this.alertas_cache !== JSON.encode(response.alertas)){
					this.alertas_cache = JSON.encode(response.alertas)
					this.zones = {0:0,1:0,2:0,3:0}
					this.zonelimit = Math.floor(sensores.length/4)
					
					this.alertas.empty()
					for(i=0;i<response.alertas.length; i++){
						alerta = new Element('li', {
							html: '<span>'+errorNames[response.alertas[i].tipo]+'</span> <span>'+response.alertas[i].num_sensor+'</span> <span>'+response.alertas[i].fecha_hora+'</span> <button data-id="'+response.alertas[i].id+'" class="revised">Revisado</button>',
							'class': 't'+response.alertas[i].tipo
							})
						cache[response.alertas[i].num_sensor] = response.alertas[i].tipo
						if(response.alertas[i].tipo > 2){
							this.zones[Math.floor(response.alertas[i].num_sensor/4)] ++
						}
						docfrag.appendChild(alerta)
					}
					this.alertas.appendChild(docfrag)
				}

				//Carga de Sensores y Fecha
				fecha = sensores.shift()
				this.fecha.set('html', fecha)

				this.sensores.empty()

				for(i=0;i<sensores.length; i++){
					sensor = new Element('li', {
						html: '<span>'+i+'['+sensores[i]+']</span> <span>'+(errorNames[cache[i]]||'OK')+'</span>',
						'class': 'sensor t'+(cache[i]||'OK'),
						'data-id': sensores[i]
						})
					docfrag2.appendChild(sensor)
				}

				this.sensores.appendChild(docfrag2)
				
				//Death Star Alert update
				for(i=0;i<=4;i++){
					if(this.zones[i]){
						$$('#deathStar .row'+i).addClass('danger')
					}else{
						$$('#deathStar .row'+i).removeClass('danger')
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
				var id = target.get('data-id'),
					parent = target.getParent('li'),
					count

				parent.set('reveal',{duration: 300})
				parent.dissolve()
				
				this.zones[Math.floor(id/4)] --

				if((count=this.zones[Math.floor(id/4)]) === 0){
					$$('#deathStar .row'+(Math.floor(id/4))).removeClass('danger')
				}

				new Request.JSON({
					url: '/mark_alert/'+id,
					onSuccess: function(){}
				}).get()
			},

			showChart: function(evt, target){
				var req = new Request.JSON({
						url: '/graph/'+target.id,
						onSuccess: function(response){
							
					})
			}
		}),
		alerta = new Alerta()
})()