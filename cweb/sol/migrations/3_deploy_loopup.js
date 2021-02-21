const Lookup = artifacts.require("Lookup");

module.exports = function (deployer) {
  deployer.deploy(Lookup);
};
