var goButton = $('#go-btn');
var results = $('#results');


goButton.click(function() {
  //alert("Button clicked");
  results.show();
});

(function() {
	var app = angular.module('yelp', []);

	app.controller('TabController', function(){
		this.tab = 1;

		this.selectTab = function(setTab) {
			this.tab = setTab;
		};

		this.isSelected = function(checkTab) {
			return this.tab === checkTab;
		}
	});

	app.controller('TableController', function($scope, $http){

		$scope.headers = ['Name', 'Stars', 'Categories', 'Image'];
		$scope.loadRecommendations = function(user) {
			if (String(user) === "Veggie Galaxy") {
				user_code = "qw5gR8vW7mSOK4VROSwdMA";
			}
			else if (String(user) === "The Back Abbey") {
				user_code = "81IjU5L-t-QQwsE38C63hQ";
			}
			else {
				alert("Sorry, that restaurant is not in our database.")
			}
			// alert(user);
      // $http.get('sample.json').success(function(data) { THIS STILL WORKS
			$http.get(user_code + '.json').success(function(data) {
				$scope.restaurants = data;
				$('#results').fadeIn();
			});
		}
		
	});

	app.directive('starRating', function () {
    return {
        restrict: 'A',
        template: '<ul class="rating">' +
            '<li ng-repeat="star in stars" ng-class="star">' +
            '\u2605' +
            '</li>' +
            '</ul>',
        scope: {
            ratingValue: '=',
            max: '='
        },
        link: function (scope, elem, attrs) {
            scope.stars = [];
            for (var i = 0; i < scope.max; i++) {
                scope.stars.push({
                    filled: i < scope.ratingValue
                });
	            }
	        }
	    }
	});

})();
