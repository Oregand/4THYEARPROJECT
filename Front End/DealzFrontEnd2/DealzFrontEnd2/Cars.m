//
//  Cars.m
//  DealzFrontEnd2
//
//  Created by David O'Regan on 18/03/2014.
//  Copyright (c) 2014 David O'Regan. All rights reserved.
//

#import "Cars.h"

@implementation Cars
@synthesize title, link, carYear, location, price, mileage, engine;

- (id) initWithTitle: (NSString *)cTitle andLink: (NSString *)cLink andCarYear: (NSString *)cYear andPrice: (NSString *)cPrice andLocation: (NSString *)cLocation andMileage: (NSString *)cMileage andEngine: (NSString *)cEngine

{
    self = [super init];
    if(self)
    {
        title = cTitle;
        link = cLink;
        carYear = cYear;
        location = cLocation;
        price = cPrice;
        mileage = cMileage;
        engine = cEngine;
        
    }
        
    return self;
}

@end
