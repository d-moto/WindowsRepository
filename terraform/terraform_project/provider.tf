## すべての環境で共通のプロバイダーを定義します。
terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.78.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
  features {}
  skip_provider_registration = true
}