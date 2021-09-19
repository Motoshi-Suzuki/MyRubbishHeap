//
//  UserInfo.swift
//  TryCombine2
//
//  Created by Motoshi Suzuki on 2021/09/17.
//

import Foundation

struct User: Decodable {
    let name: String
    let company: Company
}

struct Company: Decodable {
    let name: String
}
