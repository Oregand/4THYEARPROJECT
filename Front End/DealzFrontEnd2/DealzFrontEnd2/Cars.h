//
//  Cars.h
//  DealzFrontEnd2
//
//  Created by David O'Regan on 18/03/2014.
//  Copyright (c) 2014 David O'Regan. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Cars : NSObject

@property (strong, nonatomic) NSString * title;
@property (strong, nonatomic) NSString * link;
@property (strong, nonatomic) NSString * carYear;
@property (strong, nonatomic) NSString * price;
@property (strong, nonatomic) NSString * location;
@property (strong, nonatomic) NSString * mileage;
@property (strong, nonatomic) NSString * engine;

#pragma mark -
#pragma mark Class Methods 

- (id) initWithTitle: (NSString *)cTitle andLink: (NSString *)cLink andCarYear: (NSString *)cYear andPrice: (NSString *)cPrice andLocation: (NSString *)cLocation andMileage: (NSString *)cMileage andEngine: (NSString *)cEngine;




@end
