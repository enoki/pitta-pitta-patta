import pygame

class Mode:
    NORMAL, DRAGGING = range(2)

class CardDraggingEventHandler:
    def __init__(self, card_group):
        self.card_group = card_group
        self.mode = Mode.NORMAL
        self.selected_card = None

    def handle_card_dragging(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in [1,2,3]:
                if self.mode == Mode.NORMAL:
                    card = self.card_group.get_card(event.pos[0], event.pos[1])
                    if card:
                        self.selected_card = card
                        self.mode = Mode.DRAGGING

                        if event.button == 3:
                            card.flip()
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.mode == Mode.DRAGGING:
                self.card_group.drop_card(self.selected_card)
                self.selected_card = None
                self.mode = Mode.NORMAL
        elif event.type == pygame.MOUSEMOTION:
            if self.mode == Mode.DRAGGING:
                if event.buttons[0] or event.buttons[1] or event.buttons[2]:
                    self.selected_card.move(event.rel[0], event.rel[1])
