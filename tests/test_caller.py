from src.vaultModels.enums import Caller

def test_values():
    assert Caller.CLOUDGAME == 100
    assert Caller.RAZORPAY == 600
