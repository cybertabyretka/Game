import pygame as pg

from Utils.Image import load_image

from Models.Items.Weapons.BaseWeapon import Weapon
from Models.Items.Shield import Shield
from Models.Inventory.Inventory import Inventory


class EntityV:
    def __init__(self, paths_asset: dict[str, str]):
        self.paths_asset: dict[str, str] = paths_asset
        self.image_up: pg.Surface | None = None
        self.image_down: pg.Surface | None = None
        self.image_right: pg.Surface | None = None
        self.image_left: pg.Surface | None = None
        self.current_image: pg.Surface | None = None

    def download_images(self, current_weapon: Weapon, current_shield: Shield, inventory: Inventory) -> None:
        self.image_up = load_image(self.paths_asset['up'])
        self.image_down = load_image(self.paths_asset['down'])
        self.image_right = load_image(self.paths_asset['right'])
        self.image_left = load_image(self.paths_asset['left'])
        self.current_image = self.image_up
        if current_weapon is not None:
            current_weapon.view.download_images()
        if current_shield is not None:
            current_shield.view.download_images()
        inventory.download_images()

    def rotate(self, rotation: int) -> None:
        if rotation == 0:
            self.current_image = self.image_up
        elif rotation == 90:
            self.current_image = self.image_right
        elif rotation == 180:
            self.current_image = self.image_down
        elif rotation == 270:
            self.current_image = self.image_left

    def draw(self, surface: pg.Surface, pos: tuple[int, int]) -> None:
        surface.blit(self.current_image, pos)
