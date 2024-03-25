INSERT INTO District_Adjacencies 
(DistrictType, YieldChangeId) VALUES
('DISTRICT_PALACE_GROUNDS', 'NaturalWonder_Faith'),
('DISTRICT_PALACE_GROUNDS', 'Mountain_Faith1'),
('DISTRICT_PALACE_GROUNDS', 'Mountain_Faith2'),
('DISTRICT_PALACE_GROUNDS', 'Mountain_Faith3'),
('DISTRICT_PALACE_GROUNDS', 'Mountain_Faith4'),
('DISTRICT_PALACE_GROUNDS', 'Mountain_Faith5'),
('DISTRICT_PALACE_GROUNDS', 'Forest_Faith'),
('DISTRICT_PALACE_GROUNDS', 'Government_Faith'),
('DISTRICT_PALACE_GROUNDS', 'District_Palace_Grounds_Faith'),
('DISTRICT_PALACE_GROUNDS', 'HollowNest_TEMPLE_OF_THE_BLACK_EGG_SQUARE_Faith');

INSERT INTO Adjacency_YieldChanges 
(ID, Description, YieldType, YieldChange, TilesRequired, OtherDistrictAdjacent) VALUES
('District_Palace_Grounds_Faith', 'LOC_DISTRICT_PALACE_GROUNDS_FAITH', 'YIELD_FAITH', 1, 1, 1);

INSERT INTO District_GreatPersonPoints 
(DistrictType, GreatPersonClassType, PointsPerTurn) VALUES
('DISTRICT_PALACE_GROUNDS', 'GREAT_PERSON_CLASS_PROPHET', 1);

INSERT INTO District_CitizenYieldChanges 
(DistrictType, YieldType, YieldChange) VALUES
('DISTRICT_PALACE_GROUNDS', 'YIELD_FAITH', 2);

INSERT INTO DistrictModifiers 
(DistrictType, ModifierId) VALUES
('DISTRICT_PALACE_GROUNDS', 'PALACE_GROUNDS_FAITH');

INSERT INTO Modifiers 
(ModifierId, ModifierType) VALUES
('PALACE_GROUNDS_FAITH', 'MODIFIER_PLAYER_DISTRICT_ADJUST_BASE_YIELD_CHANGE');

INSERT INTO ModifierArguments 
(ModifierId, Name, Value) VALUES
('PALACE_GROUNDS_FAITH', 'Amount', '1'),
('PALACE_GROUNDS_FAITH', 'YieldType', 'YIELD_FAITH');
