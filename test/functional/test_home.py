
def test_index_route(app, client):
    
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Vertical Tanks Maintainance" in res.data 
        assert b"Welcome To VTM" in res.data
        


def test_about_route(app, client):
    
    
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"Verticle Tank Maintainance VTM" in res.data
        assert b"About VTM" in res.data



def test_add_estimate_route(app, client):
    
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert b"Verticle Tank Maintainance VTM" in res.data
        assert b"VTM Price Estimator" in res.data
        assert b"Radius:" in res.data

def test_add_estimate_route(app, client):
    
    with app.test_client() as test_client:
        estimate={"Radius":"180","Height":"360"}
        res = test_client.post('/estimate',data=estimate)
        assert res.status_code == 200

