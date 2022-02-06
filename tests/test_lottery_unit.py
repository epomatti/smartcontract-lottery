from brownie import Lottery, accounts, network, config
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3
import pytest
from scripts.utils import LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_get_entrance_fee():

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    # Arrange
    lottery = deploy_lottery()

    # Act
    expected_entrance_fee = Web3.toWei(0.025, "ether")
    entrance_fee = lottery.getEntranceFee()

    # Assert
    assert expected_entrance_fee == entrance_fee
